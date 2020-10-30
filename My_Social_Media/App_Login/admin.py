from django.contrib import admin
from .models import User_Profile_Model, Follow_Model

# Register your models here.

admin.site.register(User_Profile_Model)
admin.site.register(Follow_Model)
