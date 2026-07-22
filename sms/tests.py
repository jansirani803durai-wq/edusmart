from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Batch, Certificate, Course, Student


class EduTrackTests(TestCase):

    def setUp(self):
        self.batch = Batch.objects.create(
            name="Python Full Stack",
            start_date=date.today(),
        )

        self.course = Course.objects.create(
            name="Django",
            description="Django web development course",
        )

        self.student = Student.objects.create(
            first_name="Ruthuresh",
            last_name="Jagan",
            email="ruthuresh@example.com",
            phone_number="9876543210",
            batch=self.batch,
        )

        self.student.courses.add(self.course)

    def test_home_page(self):
        response = self.client.get(
            reverse("home")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_student_list(self):
        response = self.client.get(
            reverse("student_list")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            self.student.full_name,
        )

    def test_certificate_generation(self):
        certificate_url = reverse(
            "issue_certificate",
            args=[
                self.student.id,
                self.course.id,
            ],
        )

        response = self.client.get(
            certificate_url
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertEqual(
            Certificate.objects.count(),
            1,
        )