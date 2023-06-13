from django.contrib.auth.models import AbstractUser
from django.db import models


class Vehicle(models.Model):
    model = models.CharField(max_length=63)
    brand = models.CharField(max_length=63)
    year = models.CharField(max_length=63)
    vehicle_number = models.CharField(max_length=63, unique=True)
    owner = models.CharField(max_length=63)

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.model} {self.brand} ({self.vehicle_number})"


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["first_name"]
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.profession})"


class Task(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    workers = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
