from django.contrib import admin
from .models import Like_Model, Post_Model

# Register your models here.

admin.site.register(Post_Model)
admin.site.register(Like_Model)
