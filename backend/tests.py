from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Trip, User
import datetime


class FetchTripByUserIDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(
            first_name="Jimmy", last_name="Johnson", email="jj@test.com"
        )
        self.trip1 = Trip.objects.create(
            name="test1",
            start=datetime.datetime(2024, 11, 1),
            end=datetime.datetime(2024, 11, 5),
            user=self.user1,
        )
        self.trip2 = Trip.objects.create(
            name="test2",
            start=datetime.datetime(2024, 11, 1),
            end=datetime.datetime(2024, 11, 5),
            user=self.user1,
        )
        self.url = reverse("fetch_trips_by_user_id", args=[self.user1.id])

    def test_fetch_trips_by_user_id(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TripValidationTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            first_name="Iso", last_name="Joe", email="ij@test.com"
        )

    def test_invalid_trip(self):
        trip = Trip.objects.create(
            name="trip1",
            start=datetime.datetime(2024, 10, 10),
            end=datetime.datetime(2024, 10, 9),
        )
        with self.assertRaises(ValidationError):
            trip.clean()

    def test_valid_trip(self):
        trip = Trip.objects.create(
            name="trip1",
            start=datetime.datetime(2024, 10, 10),
            end=datetime.datetime(2024, 10, 11),
        )
        try:
            trip.clean()
        except ValidationError:
            self.fail("ValidationError raised for a valid trip")
