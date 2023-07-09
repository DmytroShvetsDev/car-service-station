from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordContextMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView

from service.forms import (
    WorkerCreationForm,
    WorkerUpdateForm,
    VehicleUpdateForm,
    VehicleCreateForm,
    TaskForm,
    ProfessionSearchForm,
    TaskTypeSearchForm,
    VehicleSearchForm,
    WorkerSearchForm,
    TaskSearchForm, UserPasswordChangeForm,
)
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
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProfessionsListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = ProfessionSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = ProfessionSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


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
    paginate_by = 10
    queryset = TaskType.objects.all()
    success_url = reverse_lazy("service:task-types-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypesListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskTypeSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = TaskTypeSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("service:task-types-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("service:task-types-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("service:task-types-list")


class VehiclesListView(LoginRequiredMixin, generic.ListView):
    model = Vehicle
    fields = "__all__"
    paginate_by = 10
    success_url = reverse_lazy("service:vehicles-list")
    queryset = Vehicle.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VehiclesListView, self).get_context_data(**kwargs)

        model = self.request.GET.get("model", "")

        context["search_form"] = VehicleSearchForm(initial={"model": model})

        return context

    def get_queryset(self):
        form = VehicleSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                model__icontains=form.cleaned_data["model"]
            )

        return self.queryset


class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Vehicle


class VehicleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Vehicle
    form_class = VehicleCreateForm
    success_url = reverse_lazy("service:vehicles-list")


class VehicleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Vehicle
    form_class = VehicleUpdateForm
    success_url = reverse_lazy("service:vehicles-list")


class VehicleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy("service:vehicles-list")


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10
    queryset = Worker.objects.all().select_related("profession")
    success_url = reverse_lazy("service:workers-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkersListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerSearchForm(
            initial={"username": username}
        )

        return context

    def get_queryset(self):
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )

        return self.queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("service:workers-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("service:workers-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("service:workers-list")


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    fields = "__all__"
    paginate_by = 10
    queryset = Task.objects.all().select_related("vehicle", "task_type")
    success_url = reverse_lazy("service:tasks-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = TaskTypeSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = (
        Task.objects.all()
        .prefetch_related("workers__profession")
        .select_related("task_type", "vehicle")
    )


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("service:tasks-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("service:tasks-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("service:tasks-list")


@login_required
def toggle_assign_to_task(request, pk):
    worker = Worker.objects.get(id=request.user.id)
    if Task.objects.get(id=pk) in worker.tasks.all():
        worker.tasks.remove(pk)
    else:
        worker.tasks.add(pk)
    return HttpResponseRedirect(reverse_lazy("service:task-detail", args=[pk]))


@login_required()
def update_task_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("service:task-detail", pk=pk)


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = UserPasswordChangeForm


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "accounts/password_change_done.html"
    title = "Password change successful"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
