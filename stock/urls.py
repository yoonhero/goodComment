from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('confirm', views.confirm, name="confirm"),
    path('sitemap.xml', views.sitemap, name="sitemap"),
    path('robots.txt', views.robot, name="robot"),
    path('favicon.ico', views.icon, name="icon"),
]
