from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('update_item/', views.updateItem, name='update_item')
]
    