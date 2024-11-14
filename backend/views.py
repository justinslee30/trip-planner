from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer


@api_view(["GET"])
def fetch_trip_by_user_id(request, user_id):
    """
    Retrieve all trips for user with id `user_id`
    """
    try:
        trips = Trip.objects.filter(user_id=user_id)
        trips_serialized = TripSerializer(trips, many=True)
        return Response(trips_serialized.data)
    except Trip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
