from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from service.models import Vehicle, TaskType, Profession, Worker, Task

TASK_LIST_URL = reverse("service:tasks-list")


class PrivateTaskListTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            model="Lanos",
            brand="Daewoo",
            year="2001",
            vehicle_number="XX2222YY",
            owner="Petro",
        )
        self.task_type = TaskType.objects.create(
            name="Oil change"
        )
        self.profession = Profession.objects.create(
            name="Engine master"
        )
        self.worker = Worker.objects.create_user(
            username="Username",
            password="Password1234",
            first_name="Petro",
            last_name="Stus",
            profession=self.profession,
        )
        self.task = Task.objects.create(
            name="New task",
            description="Some description",
            vehicle=self.vehicle,
            task_type=self.task_type,
        )
        self.task.workers.add(self.worker)

        self.client.force_login(self.worker)


    def test_retrieve_tasks(self):
        response = self.client.get(TASK_LIST_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )

    def test_search_task(self):
        response = self.client.get(TASK_LIST_URL, {"name": "new"})
        search_task = Task.objects.filter(name="New task")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(search_task)
        )


class PublicTaskListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
