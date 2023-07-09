from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from service.models import Vehicle

VEHICLES_LIST_URL = reverse("service:vehicles-list")


class PrivateVehiclesListTest(TestCase):
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username="Testuser", password="Test12345"
        )

        self.client.force_login(self.user)

    def test_retrieve_vehicle(self):

        response = self.client.get(VEHICLES_LIST_URL)
        vehicles = Vehicle.objects.all()[:10]
        print(vehicles)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["vehicle_list"]),
            list(vehicles)
        )

    def test_search_vehicle(self):

        response = self.client.get(VEHICLES_LIST_URL, {"model": "octavia"})
        search_vehicle = Vehicle.objects.filter(model__icontains="octavia")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["vehicle_list"]),
            list(search_vehicle)
        )


class PublicVehicleListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(VEHICLES_LIST_URL)

        self.assertNotEqual(response.status_code, 200)
