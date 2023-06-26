from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from service.models import Worker, Vehicle


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


class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"

    def clean_vehicle_number(self):
        return validate_vehicle_number(self.cleaned_data["vehicle_number"])


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"

    def clean_vehicle_number(self):
        return validate_vehicle_number(self.cleaned_data["vehicle_number"])


def validate_vehicle_number(
    vehicle_number,
):
    if len(vehicle_number) != 8:
        raise ValidationError("Vehicle number should consist of 8 characters")
    elif not vehicle_number[:2].isalpha() or not vehicle_number[:2].isupper():
        raise ValidationError("First 2 characters should be uppercase letters")
    elif not vehicle_number[2:6].isdigit():
        raise ValidationError("Characters 3 to 6 should be digits")
    elif not vehicle_number[6:].isalpha() or not vehicle_number[6:].isupper():
        raise ValidationError("Last 2 characters should be uppercase letters")

    return vehicle_number
