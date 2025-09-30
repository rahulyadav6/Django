from django.urls import path
from . import views

urlpatterns = [
    path('convert_temp/<str:unit>/<str:value>', views.convert_temp, name='convert_temp'),
]