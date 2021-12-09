from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('listings/<int:id>', views.listing, name='listing'),
    path('search/', views.search, name="search_results"),
    path('quicksearch/', views.quick_search, name="quick_search")
]
