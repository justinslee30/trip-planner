from django.contrib import admin
from .models import Trip, User


class TripAdmin(admin.ModelAdmin):
    trip_display = ("name", "start", "end")


class UserAdmin(admin.ModelAdmin):
    user_display = ("first_name", "middle_name", "last_name", "email")


admin.site.register(Trip, TripAdmin)
admin.site.register(User, UserAdmin)
