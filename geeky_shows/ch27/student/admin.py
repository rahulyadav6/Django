from django.contrib import admin
from student.models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','First_name','Last_name', 'Email','City')