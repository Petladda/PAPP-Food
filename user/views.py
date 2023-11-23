
from django.urls import reverse
from django.contrib.auth import login
from django.http.response import HttpResponse
from django.http import HttpRequest,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from . forms import CustomerRegisterForm
from django.contrib import messages
from . models import *
from menufoods.models import Food
import json


# Create your views here.
def regidter(request: HttpRequest):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"User Register Successfully")
            login(request,user)
            
            return HttpResponseRedirect(reverse("home"))
    else:
        messages.error(request,"Invalid Input Data")
        form = CustomerRegisterForm()

    
    context = {'form':form}
    return render(request, 'user/register.html',context)


def show_cart(request: HttpRequest):
    if request.user.is_authenticated:
       user = request.user
       order, created = Order.objects.get_or_create(user=user , complete=False)
       items = order.orderitem_set.all()
        
    else:
        items = []
        order = {'total_item': 0, 'total_price': 0}
    context={'items':items, 'order':order}
    return render(request,'user/addtocart.html',context)


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


def orderlist(request : HttpRequest):
	if request.user.is_authenticated:
		user = request.user
		order, created = Order.objects.get_or_create(user=user, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0 }

	context = {'items':items, 'order':order}
	return render (request, 'user/orderlist.html', context)


