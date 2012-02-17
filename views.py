# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from Drinks.models import Drink, Amount
from Drinks.utils import searchParse

# STD imports
import time
import random
random.seed(time.time())

def quiz(request):
    drinks = Drink.objects.all()
    drink_id = random.randint(0,drinks.count()-1)
    d = drinks[drink_id]
    return render_to_response("Drinks/quiz.html",{'drink':d})


def drink(request, drink_slug):
    d = get_object_or_404(Drink,slug__iexact=drink_slug,variation=1)
    return render_to_response("Drinks/drink.html",{'drink':d})


def search(request):
    d_list,g_list,i_list,query = (None,None,None,"")
    if request.GET:
        query = request.GET['drink_name']
        if query:
            d_list,g_list,i_list = searchParse(query)
    return render_to_response("Drinks/search.html",{'d_list':d_list,
                                                    'g_list':g_list,
                                                    'i_list':i_list,
                                                    'query' :query})
