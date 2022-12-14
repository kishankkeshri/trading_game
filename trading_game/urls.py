"""trading_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/',views.home, name='home'),
    path('user_created/',views.user_created, name='user_created'),
    path('leaderboard/',views.leaderboard, name='leaderboard'),
    path('logout/', views.logout, name='logout'),
    path('portfoliostock/' ,views.portfoliostock, name="portfo")
 
] 
