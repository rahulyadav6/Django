from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('technology/', views.technology, name="technology"),
    path('sports/', views.sports, name="sports"),
    path('politics/', views.politics, name="politics"),
    path('entertainment/', views.entertainment, name="entertainment"),
]