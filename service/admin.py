from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from service.models import Vehicle, TaskType, Profession, Worker, Task


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    search_fields = (
        "model",
        "brand",
    )
    list_display = (
        "model",
        "brand",
        "year",
        "vehicle_number",
        "owner",
    )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("profession",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("profession",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email",
                        "profession",
                    )
                },
            ),
        )
    )
    list_filter = UserAdmin.list_filter + ("profession",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("task_type",)
    list_display = (
        "name",
        "description",
        "deadline",
        "is_completed",
        "vehicle",
        "task_type",
    )
    list_filter = ("task_type",)
