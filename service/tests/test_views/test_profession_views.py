from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from service.models import Profession


PROFESSIONS_URL = reverse("service:professions-list")


class PrivateProfessionsListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Profession.objects.create(name="Engine master")
        Profession.objects.create(name="Wheels master")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Testuser", password="Test12345"
        )

        self.client.force_login(self.user)

    def test_retrieve_profession(self):
        response = self.client.get(PROFESSIONS_URL)
        professions = Profession.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["professions_list"]), list(professions))

    def test_search_profession(self):
        response = self.client.get(PROFESSIONS_URL, {"name": "engine"})
        search_profession = Profession.objects.filter(name="Engine master")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["professions_list"]), list(search_profession)
        )


class PublicProfessionsListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(PROFESSIONS_URL)

        self.assertNotEqual(response.status_code, 200)
