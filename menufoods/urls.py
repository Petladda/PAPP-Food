from django.urls import path
from . import views

urlpatterns =[
    path('', views.menufoods, name='manufoods'),
    path('<int:food_id>', views.food, name='food'),
    path('update_item/', views.updateItem, name='update_item'),
    
    
    
]