'''
@author:Yusuke Tsutsumi
'''

from Drinks.models import Glass, Garnish, IngredientType, \
    Ingredient, Drink, Amount
from django.contrib import admin

admin.site.register(Glass)
admin.site.register(Garnish)
admin.site.register(IngredientType)
admin.site.register(Ingredient)
admin.site.register(Drink)
admin.site.register(Amount)


