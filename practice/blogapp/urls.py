from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/', views.blog, name='blog'),
    path('<slug:slug>/', views.view_post, name='view_post'),
]
