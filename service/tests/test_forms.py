from django.core.exceptions import ValidationError
from django.test import TestCase

from service.forms import validate_vehicle_number, VehicleCreateForm, VehicleUpdateForm
from service.models import Vehicle


class VehicleNumberValidationTestCase(TestCase):
    def setUp(self):
        self.form_data = {
            "model": "Lanos",
            "brand": "Daewoo",
            "year": "2001",
            "vehicle_number": "XX2222YY",
            "owner": "Petro",
        }

    def test_valid_vehicle_create_form(self):
        form = VehicleCreateForm(data=self.form_data)

        self.assertTrue(form.is_valid())

    def test_valid_vehicle_update_form(self):
        form = VehicleUpdateForm(data=self.form_data)

        self.assertTrue(form.is_valid())

    def test_invalid_length(self):
        form = VehicleUpdateForm(
            data={
                "model": "Lanos",
                "brand": "Daewoo",
                "year": "2001",
                "vehicle_number": "XX2222YYw",
                "owner": "Petro",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("vehicle_number", form.errors)
        self.assertEqual(
            form.errors["vehicle_number"],
            ["Vehicle number should consist of 8 characters"],
        )

    def test_invalid_first_charters(self):
        form = VehicleUpdateForm(
            data={
                "model": "Lanos",
                "brand": "Daewoo",
                "year": "2001",
                "vehicle_number": "Xf2222YY",
                "owner": "Petro",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("vehicle_number", form.errors)
        self.assertEqual(
            form.errors["vehicle_number"],
            ["First 2 characters should be uppercase letters"],
        )

    def test_invalid_last_charters(self):
        form = VehicleUpdateForm(
            data={
                "model": "Lanos",
                "brand": "Daewoo",
                "year": "2001",
                "vehicle_number": "XR222299",
                "owner": "Petro",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("vehicle_number", form.errors)
        self.assertEqual(
            form.errors["vehicle_number"],
            ["Last 2 characters should be uppercase letters"],
        )

    def test_invalid_3_to_6_charters(self):
        form = VehicleUpdateForm(
            data={
                "model": "Lanos",
                "brand": "Daewoo",
                "year": "2001",
                "vehicle_number": "RRXXXXRR",
                "owner": "Petro",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("vehicle_number", form.errors)
        self.assertEqual(
            form.errors["vehicle_number"],
            ["Characters 3 to 6 should be digits"],
        )
