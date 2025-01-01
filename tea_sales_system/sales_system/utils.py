from decimal import Decimal
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import now
from scipy.spatial.distance import cosine
import numpy as np


class Cart:
    from product_management.models import Product
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            promotions = [promo.id for promo in product.promotion.all()]
            self.cart[product_id] = {
                'quantity': quantity,
                'price': float(product.sales_price),
                'promotions': promotions
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        from product_management.models import Product
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            cart_item = self.cart[str(product.id)]
            promotions = [promo.id for promo in product.promotion.all()]
            yield {
                'product': product,
                'quantity': cart_item['quantity'],
                'price': Decimal(cart_item['price']),
                'total_price': Decimal(cart_item['price'] * cart_item['quantity']),
                'promotions': promotions
            }

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """计算购物车的总价格"""
        return sum(
            Decimal(item['price']) * item['quantity'] for item in self.cart.values()
        )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


def get_user_ratings_matrix():
    from order_management.models import Evaluation
    from product_management.models import Product
    from user_management.models import User
    # 获取所有评分数据并生成用户-商品评分矩阵
    ratings = Evaluation.objects.all()
    users = list(User.objects.all())
    products = list(Product.objects.all())

    user_ratings = np.zeros((len(users), len(products)))

    # 填充用户评分矩阵
    for rating in ratings:
        user_index = users.index(rating.user)
        product_index = products.index(rating.product)
        user_ratings[user_index, product_index] = rating.score

    return user_ratings, users, products

def calculate_similarity(user_ratings):
    # 计算用户相似性矩阵（余弦相似度）
    num_users = user_ratings.shape[0]
    similarity_matrix = np.zeros((num_users, num_users))

    for i in range(num_users):
        for j in range(num_users):
            if i != j:
                # 使用余弦相似度
                if np.linalg.norm(user_ratings[i]) > 0 and np.linalg.norm(user_ratings[j]) > 0:
                    similarity_matrix[i, j] = 1 - cosine(user_ratings[i], user_ratings[j])

    return similarity_matrix

def recommend_products(user_id, num_recommendations=5):
    user_ratings, users, products = get_user_ratings_matrix()
    similarity_matrix = calculate_similarity(user_ratings)

    user_index = [i for i, user in enumerate(users) if user.id == user_id][0]

    # 计算加权评分预测
    user_similarity_scores = similarity_matrix[user_index]
    weighted_ratings = np.dot(user_similarity_scores, user_ratings) / np.sum(user_similarity_scores)

    # 排序并返回评分最高的未评分商品
    user_rated_products = user_ratings[user_index] > 0
    recommended_product_indices = np.argsort(weighted_ratings * ~user_rated_products)[::-1][:num_recommendations]

    recommended_products = [products[i] for i in recommended_product_indices]
    return recommended_products
