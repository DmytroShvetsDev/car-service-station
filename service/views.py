from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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


class ProfessionsListView(LoginRequiredMixin, generic.ListView):
    model = Profession
    context_object_name = "professions_list"
    template_name = "service/professions_list.html"
    queryset = Profession.objects.all()


class ProfessionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Profession
    fields = "__all__"
    success_url = reverse_lazy("service:professions-list")


class ProfessionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profession
    fields = "__all__"
    success_url = reverse_lazy("service:professions-list")


class ProfessionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Profession
    success_url = reverse_lazy("service:professions-list")


class TaskTypesListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "tasktypes_list"
    fields = "__all__"
    success_url = reverse_lazy("service:tasktypes-list")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("service:tasktypes-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("service:tasktypes-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("service:tasktypes-list")


class VehiclesListView(LoginRequiredMixin, generic.ListView):
    model = Vehicle
    fields = "__all__"
    success_url = reverse_lazy("service:vehicles-list")


class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Vehicle


class VehicleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Vehicle
    fields = "__all__"
    success_url = reverse_lazy("service:vehicles-list")


class VehicleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Vehicle
    fields = "__all__"
    success_url = reverse_lazy("service:vehicles-list")


class VehicleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy("service:vehicles-list")
