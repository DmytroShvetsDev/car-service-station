from django.urls import path

from service.views import index, ProfessionsListView, ProfessionsCreateView, ProfessionUpdateView, ProfessionDeleteView

urlpatterns = [
    path("", index, name="index"),
    path(
        "professions/",
        ProfessionsListView.as_view(),
        name="professions-list",
    ),
    path(
        "professions/create/",
        ProfessionsCreateView.as_view(),
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

]


app_name = "service"
