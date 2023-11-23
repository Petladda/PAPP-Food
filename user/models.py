

from django.db import models
from django.contrib.auth.models import User
from menufoods.models import Food
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True,null=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    
    def __self__(self):
        return self(self.id)
    
    @property
    def total_price_discount(self):
        orderitems = self.orderitem_set.all()
        quantity = sum([item.quantity for item in orderitems])
        if quantity >= 4:
            total = sum([item.total_cost for item in orderitems] ) * 0.8
        else:
            total = sum([item.total_cost for item in orderitems] ) 
        
        return total
    
    @property
    def total_price(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.total_cost for item in orderitems] )
        return total

    @property
    def total_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    food = models.ForeignKey(Food,on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)

    

    @property
    def total_cost(self):
        if self.food.special_price:
           total = self.food.special_price * self.quantity 
        else:
            total = self.food.price * self.quantity
        return total


