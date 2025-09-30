from django.urls import path
from . import views
urlpatterns = [
    #Add task
    path('addTask/', views.addTask, name='addTask'),
]
