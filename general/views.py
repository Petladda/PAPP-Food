from django.http.response import HttpResponse
from django.http import HttpRequest,HttpResponseRedirect,JsonResponse

from django.shortcuts import render
from menufoods.models import *
from user.models import *
from user.views import *

import json


# Create your views here.
def home(request : HttpRequest):

    if request.user.is_authenticated:
       user = request.user
       order, created = Order.objects.get_or_create(user=user , complete=False)
       items = order.orderitem_set.all() 
       
    else:
        items = []
        order = {'total_item': 0, 'total_price': 0}
        

    special_foods = Food.objects.order_by('special_price')
    premium_food = Food.objects.order_by('is_premium')
    context = {'home': special_foods,'home':premium_food,'items':items, 'order':order }
    return render(request, 'general/home.html',context)



def aboutus(reqest):
    return render(reqest, 'general/aboutus.html')


def updateItem(request: HttpRequest):
    data = json.loads(request.body)
    foodId = data['foodId']
    action = data['action']
    print('Action:', action)
    print('foodId:', foodId)

    user = request.user
    food = Food.objects.get(id=foodId)
    order, created = Order.objects.get_or_create(user=user , complete=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order, food=food)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)