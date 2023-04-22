from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from user.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass

