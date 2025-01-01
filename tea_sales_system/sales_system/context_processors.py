def cart_item_count(request):
    cart = request.session.get('cart', {})
    if isinstance(cart, dict):  # 确保 cart 是字典
        # 如果是简单字典结构
        try:
            count = sum(cart.values())
        except TypeError:
            # 如果是复杂嵌套字典
            count = sum(item.get("quantity", 0) for item in cart.values())
    else:
        count = 0
    return {'cart_item_count': count}
