from django.urls import include,path
from . import views

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register',view=views.regidter,name='register'),
    path('cart/',views.show_cart,name='showcart'),
    path('oder/', views.orderlist,name='orderlist'),
    
    path('update_item/', views.updateItem, name='update_item'),
    
]