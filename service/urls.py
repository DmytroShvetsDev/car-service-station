from django.urls import path

from service.views import (
    index,
    ProfessionsListView,
    ProfessionCreateView,
    ProfessionUpdateView,
    ProfessionDeleteView,
    TaskTypesListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "professions/",
        ProfessionsListView.as_view(),
        name="professions-list",
    ),
    path(
        "professions/create/",
        ProfessionCreateView.as_view(),
        name="profession-create",
    ),
    path(
        "professions/<int:pk>/update/",
        ProfessionUpdateView.as_view(),
        name="profession-update",
    ),
    path(
        "professions/<int:pk>/delete/",
        ProfessionDeleteView.as_view(),
        name="profession-delete",
    ),
    path(
        "tasktypes/",
        TaskTypesListView.as_view(),
        name="tasktypes-list",
    ),
    path(
        "tasktypes/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "tasktypes/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "tasktypes/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),

]


app_name = "service"
