'''
@author: Yusuke Tsutsumi (yusuke@yusuketsutsumi.com)
'''
from django.db import models

# Create your models here.


class Glass(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Garnish(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class IngredientType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    ingredient_type = models.ForeignKey(IngredientType)

    def __unicode__(self):
        return self.name

    def url(self):
        return "drink/" + self.name


class Drink(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    glass = models.ForeignKey(Glass)
    ice = models.BooleanField(default=False)
    garnishes = models.ManyToManyField(Garnish)
    ingredients = models.ManyToManyField(Ingredient, through='Amount')
    special = models.CharField(max_length=1000)
    variation = models.IntegerField()
    cached_text = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.name


class Amount(models.Model):
    drink = models.ForeignKey(Drink)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=50)

    def __unicode__(self):
        return "(" + self.drink.name + ") " + self.amount + " " + self.ingredient.name
