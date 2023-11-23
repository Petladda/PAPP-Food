from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'complete']

@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ['food', 'order', 'quantity']

