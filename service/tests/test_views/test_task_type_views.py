from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from service.models import TaskType

TASK_TYPES_LIST_URL = reverse("service:task-types-list")


class PrivateTaskTypesListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TaskType.objects.create(name="Change oil")
        TaskType.objects.create(name="Change wheels")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Testuser", password="Test12345"
        )

        self.client.force_login(self.user)

    def test_retrieve_task_type(self):
        response = self.client.get(TASK_TYPES_LIST_URL)
        task_types = TaskType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tasktypes_list"]),
            list(task_types)
        )

    def test_search_task_type(self):
        response = self.client.get(TASK_TYPES_LIST_URL, {"name": "oil"})
        search_task_type = TaskType.objects.filter(name="Change oil")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tasktypes_list"]), list(search_task_type)
        )


class PublicTaskTypesListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(TASK_TYPES_LIST_URL)

        self.assertNotEqual(response.status_code, 200)
