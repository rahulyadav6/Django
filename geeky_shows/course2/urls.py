from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('dj/', views.learn_django, name='learn_django'),
    path('py/', views.learn_python, name='learn_python'),
]