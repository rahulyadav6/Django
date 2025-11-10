from django.db import models

# Create your models here.
class Profile(models.Model):
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    City = models.CharField(max_length=255)