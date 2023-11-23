from django.contrib import admin
from menufoods.models import Food

# Register your models here.

class Foodadmin(admin.ModelAdmin):
    list_display = ['name','discription', 'price' ,'special_price','is_premium','image']
    search_fields = ['name']
    list_filter = ['is_premium']

admin.site.register(Food,Foodadmin)