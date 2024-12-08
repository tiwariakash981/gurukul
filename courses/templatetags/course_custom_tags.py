from django import template
from math import floor 


register = template.Library()

@register.simple_tag
def cal_sellprice(price,discount):
    if discount is None or discount is 0:
        return price
    sellprice = price - (price * discount*0.01)
    return floor(sellprice)

@register.filter
def rupee(price):
    return f' ${price} '
    

