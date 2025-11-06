from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('addbook/', views.addbook, name='addbook'),
]