from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from service.models import Vehicle, Worker, Task, TaskType, Profession


@login_required
def index(request):
    """View function for the home page of the site."""

    num_vehicles = Vehicle.objects.count()
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_tasktypes = TaskType.objects.count()
    num_professions = Profession.objects.count()


    context = {
        "num_vehicles": num_vehicles,
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_tasktypes": num_tasktypes,
        "num_professions": num_professions,
    }

    return render(request, "service/index.html", context=context)
