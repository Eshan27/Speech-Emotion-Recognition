from django.conf.urls import url
from django.contrib import admin

from django.urls import path

from.import views
urlpatterns = [
    path('', views.hi , name='home-page'),
    path('abcd/',views.products,name='products'),
    path('contact_us/', views.about , name='home-about'),
    
    path('upload/',views.upload,name='upload'),
    path('record/',views.record,name='record'),
    path('<str:id>/',views.prediction,name='prediction'),
];
