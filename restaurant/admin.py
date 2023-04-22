from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from restaurant.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(ModelAdmin):
    pass
