from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name="register"),
    path('information/', views.account_info, name="acc_info"),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/loggedout.html',
    ), name="logout"),
]
