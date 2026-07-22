# Q11 and Q21: Django ModelForms
from django import forms

from .models import Attendance, Batch, Course, Student


class DateInput(forms.DateInput):
    input_type = "date"


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            "name",
            "start_date",
        ]
        widgets = {
            "start_date": DateInput(),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "name",
            "description",
        ]
        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 4},
            ),
        }


# Q11: Student registration form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "batch",
            "courses",
        ]
        widgets = {
            "courses": forms.CheckboxSelectMultiple(),
        }


# Q21: Attendance form
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            "student",
            "date",
            "status",
        ]
        widgets = {
            "date": DateInput(),
        }
