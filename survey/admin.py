from django.contrib import admin

from .models import User, Survey

# Register your models here.

admin.site.register(User)
admin.site.register(Survey)
