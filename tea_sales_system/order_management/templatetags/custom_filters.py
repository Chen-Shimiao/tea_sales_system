from django import template

from order_management.models import Evaluation

register = template.Library()

@register.filter
def is_reviewed(order, product):
    return Evaluation.objects.filter(order=order, product=product).exists()