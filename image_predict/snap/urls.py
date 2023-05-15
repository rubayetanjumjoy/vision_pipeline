
from django.contrib import admin
from django.urls import path
from .apis import *








urlpatterns = [
   
    path('predictions/', SnapApiView.as_view(), name ='predictions'),
]

