from django.urls import path
from . import views

# urlpatterns = [
#     path('contact1/', views.contact_form_httpresponse, name='contact1'),
#     path('contact2/', views.contact_form_httpresponse, name='contact2')
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('contact/', views.contactview, name='contact'),
]