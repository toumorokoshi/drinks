# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from Drinks.models import Drink, Amount

# STD imports
import time
import random
random.seed(time.time())

def quiz(request):
    drinks = Drink.objects.all()
    drink_id = random.randint(0,drinks.count()-1)
    d = drinks[drink_id]
    return render_to_response("Drinks/quiz.html",{'drink':d,
                                                  'ingredients':Amount.objects.filter(drink=d)})
