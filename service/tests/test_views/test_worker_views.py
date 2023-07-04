from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from service.models import Worker

WORKER_LIST_URL = reverse("service:workers-list")


class PrivateWorkerListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Bob",
            password="Test12345",
        )
        self.user = get_user_model().objects.create_user(
            username="Dylan",
            password="Test12343",
        )

        self.client.force_login(self.user)

    def test_retrieve_workers(self):
        response = self.client.get(WORKER_LIST_URL)
        workers = Worker.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["worker_list"]), list(workers))

    def test_search_workers(self):
        response = self.client.get(WORKER_LIST_URL, {"username": "Bob"})
        search_worker = Worker.objects.filter(username="Bob")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(search_worker)
        )


class PublicWorkerListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
