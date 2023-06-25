from django import forms
from django.contrib.auth.forms import UserCreationForm

from service.models import Worker


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "profession",
            "first_name",
            "last_name",
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "username",
            "profession",
            "first_name",
            "last_name",
        ]
