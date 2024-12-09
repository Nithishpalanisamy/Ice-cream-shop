from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_suggestion/', views.add_suggestion, name='add_suggestion'),
    path('add_allergen/', views.add_allergen, name='add_allergen'),
    path('cart/', views.manage_cart, name='cart'),
    path('search/', views.search_flavors, name='search_flavors'),
]
