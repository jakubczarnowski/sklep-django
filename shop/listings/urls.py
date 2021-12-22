from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.index, name='index'),
    path('listings/<int:id>', views.listing, name='listing'),
    path('search/', views.search, name="search_results"),
    path('quicksearch/', views.quick_search, name="quick_search"),
    path('category/<int:id>', views.category, name="category"),
    path('updateCart/', views.update_cart_item, name="update_cart_item"),
    path('cart/', views.cart_view, name="cart"),
]
