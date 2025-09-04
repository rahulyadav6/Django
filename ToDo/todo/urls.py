from django.urls import path
from . import views
urlpatterns = [
    path('addTasks/', views.addTask, name='addTask'),
]
