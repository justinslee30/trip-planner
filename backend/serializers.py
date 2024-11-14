from rest_framework import serializers
from .models import Trip, User


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ("id", "name", "start", "end")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "middle_name", "last_name", "email")
