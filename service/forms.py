from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from service.models import Worker, Vehicle, Task


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


class TaskForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline <= timezone.now():
            raise ValidationError("The deadline cannot be in the past")
        return deadline

    class Meta:
        model = Task
        fields = "__all__"


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by task name"}),
    )


class VehicleSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by model"}),
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by task type"}),
    )


class ProfessionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by profession"}),
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Old Password'
    }), label="New Password")
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")
