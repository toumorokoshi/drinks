'''
@author: Yusuke Tsutsumi (yusuke@yusuketsutsumi.com)
'''
import xml.etree.ElementTree as xml
from Drinks.models import Glass, Garnish, IngredientType, Ingredient, Drink, Amount
import re
import unittest


def convertXMLToDrinks(filepath):
    """ Converts the xml file specified in filepath
        to the drinks model
    """
    drinks_xml = xml.parse(filepath)
    root = drinks_xml.getroot()
    drink_xlist = root.findall("drink")
    for drink_x in drink_xlist:
        d = Drink()
        d.name = drink_x.get('name')
        d.slug = toSlug(d.name)
        # parse for new glass type
        try:
            g = Glass.objects.get(name=drink_x.get('glass').lower())
        except Glass.DoesNotExist:
            g = Glass()
            g.name = drink_x.get('glass').lower()
            g.save()
        d.glass = g
        # parse for ice
        d.ice = (True if (drink_x.get('ice') is not None and drink_x.get('ice').lower().startswith('t')) else False)
        # parse for garnishes
        d.variation = (1 if drink_x.get('variation') is None else int(drink_x.get('variation')))
        d.save()
        garnishes_xlist = drink_x.findall("garnish")
        for garnish_x in garnishes_xlist:
            try:
                ga = Garnish.objects.get(name=garnish_x.text.lower())
            except:
                ga = Garnish()
                ga.name = garnish_x.text.lower()
                ga.save()
            d.garnishes.add(ga)
        # parse for ingredients (drink must be saved at this point to continue)
        d.special = ("" if not drink_x.get('special') else drink_x.get('special'))
        d.save()
        ingredient_xlist = drink_x.findall("ingredient")
        for ingredient_x in ingredient_xlist:
            try:
                i = Ingredient.objects.get(name=ingredient_x.text.lower())
            except:
                i = Ingredient()
                i.name = ingredient_x.text.lower()
                try:
                    it = IngredientType.objects.get(name=ingredient_x.get('type').lower())
                except:
                    it = IngredientType()
                    it.name = ingredient_x.get('type').lower()
                    it.save()
                i.ingredient_type = it
                i.save()
            a = Amount()
            a.drink = d
            a.ingredient = i
            a.amount = ingredient_x.get('amount')
            a.save()
    return


def searchParse(q_string):
    """ Parsing the query string passed through search
        rules:
        colons are used to classify query type
    """
    # example string
    # drink:margarita alcohol:tequila garnish:cherries
    # margarita,alcohol:tequila
    d_list = Drink.objects.filter(name__icontains=q_string)
    garnishes = Garnish.objects.filter(name__icontains=q_string)
    ingredients = Ingredient.objects.filter(name__icontains=q_string)
    g_list = []
    for g in garnishes:
        g_list.extend(Drink.objects.filter(garnishes=g))
    i_list = []
    for i in ingredients:
        i_list.extend(Drink.objects.filter(ingredients=i))
    return (d_list, g_list, i_list)


def toSlug(s):
    """ Converts a string s to a slugworthy name:
        no spaces
        anything between parentheses is removed
        all lowercase
    """
    s = s.lower()  # lowercase
    s = s.replace(' ', '')  # remove spaces
    s = re.sub('\(.*\)', '', s)
    return s
