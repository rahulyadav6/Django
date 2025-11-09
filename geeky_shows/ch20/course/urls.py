from django.urls import path
from . import views
urlpatterns = [
    path('dj/', views.learn_django, name='dj'),
    path('py/', views.learn_python, name='py'),
]
