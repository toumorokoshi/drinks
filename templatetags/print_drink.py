from django import template
from django.conf import settings 

from Drinks.models import Drink,Amount

register = template.Library()

@register.inclusion_tag('Drinks/templatetag_drink.html')
def print_drink(drink):
    return { 'drink' : drink,
             'ingredients': Amount.objects.filter(drink=drink) }
