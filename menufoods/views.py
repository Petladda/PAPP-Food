from django.http.response import HttpResponse
from django.http import HttpRequest,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from .models import Food
from user.models import *
from user.views import *
import json

# Create your views here.
def menufoods(request):
    if request.user.is_authenticated:
       user = request.user
       order, created = Order.objects.get_or_create(user=user , complete=False)
       items = order.orderitem_set.all() 
       
    else:
        items = []
        order = {'total_item': 0, 'total_price': 0}

    all_foods = Food.objects.order_by('-is_premium','-special_price')
    context = {'menufoods': all_foods,'items':items, 'order':order}
    return render(request, 'menufoods/menufoods.html', context)

def food(request, food_id):
    if request.user.is_authenticated:
       user = request.user
       order, created = Order.objects.get_or_create(user=user , complete=False)
       items = order.orderitem_set.all() 
       
    else:
        items = []
        order = {'total_item': 0, 'total_price': 0}
    one_food = None
    try:
       one_food = Food.objects.get(id=food_id)
    except:
        print('***ไม่พบเมนูดังกล่าว โปรดเลือกเมนูอื่น***')
    context = {'food': one_food,'items':items, 'order':order}
    return render(request, 'menufoods/food.html', context)

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



