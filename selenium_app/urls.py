from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'selenium_app'

urlpatterns = [
    path("search/", views.search, name= "search"),
]