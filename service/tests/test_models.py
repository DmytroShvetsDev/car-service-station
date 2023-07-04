from django.test import TestCase

from service.models import Vehicle, TaskType, Profession, Worker, Task


class ModelsStrTests(TestCase):
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

    def test_vehicle_str(self):
        self.assertEqual(
            str(self.vehicle),
            f"{self.vehicle.model} {self.vehicle.brand} ({self.vehicle.vehicle_number})"
        )

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Oil change")

    def test_profession_str(self):
        self.assertEqual(str(self.profession), "Engine master")

    def test_worker_str(self):
        self.assertEqual(
            str(self.worker),
            f"{self.worker.first_name} {self.worker.last_name} ({self.worker.profession})"
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), "New task")
