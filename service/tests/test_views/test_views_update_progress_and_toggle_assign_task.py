from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.http import HttpResponseRedirect

from service.models import Worker, Task, Profession, TaskType, Vehicle
from service.views import toggle_assign_to_task


class TaskTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.vehicle = Vehicle.objects.create(
            model="Lanos",
            brand="Daewoo",
            year="2001",
            vehicle_number="XX2222YY",
            owner="Petro",
        )
        self.profession = Profession.objects.create(name="Test Profession")
        self.worker = Worker.objects.create_user(
            username="Worker1",
            password="Password123",
            profession=self.profession
        )
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.task = Task.objects.create(name="Test Task", task_type=self.task_type, vehicle=self.vehicle)


class ToggleAssignToTaskTest(TaskTestCase):
    def test_toggle_assign_to_task(self):
        request = self.factory.get(reverse("service:toggle-task-assign", args=[self.task.pk]))
        request.user = self.worker

        self.assertNotIn(self.task, self.worker.tasks.all())

        response = toggle_assign_to_task(request, self.task.pk)

        self.assertIn(self.task, self.worker.tasks.all())
        self.assertEqual(response.status_code, HttpResponseRedirect.status_code)
        self.assertEqual(response.url, reverse("service:task-detail", args=[self.task.pk]))


class UpdateTaskProgressTest(TaskTestCase):
    def test_update_task_progress(self):
        self.assertFalse(self.task.is_completed)
        self.client.force_login(self.worker)
        response = self.client.get(reverse("service:update-task-progress", args=[self.task.pk]))

        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)
        self.assertRedirects(response, reverse("service:task-detail", args=[self.task.pk]))
