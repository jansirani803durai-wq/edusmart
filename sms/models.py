# Q6, Q7, Q8, Q41, Q42, Q43: Database models
from django.core.exceptions import ValidationError
from django.db import models


# Q6: Batch model
class Batch(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
    )
    start_date = models.DateField()

    class Meta:
        ordering = ["-start_date", "name"]

    def __str__(self):
        return self.name


# Q41: Course model
class Course(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
    )
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# Q7: Student model
class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name="students",
    )

    # Q42: Many-to-many relationship between students and courses.
    courses = models.ManyToManyField(
        Course,
        related_name="students",
        blank=True,
    )

    class Meta:
        ordering = ["first_name", "last_name"]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.full_name


# Q8: Attendance model
class Attendance(models.Model):
    STATUS_PRESENT = "Present"
    STATUS_ABSENT = "Absent"
    STATUS_LATE = "Late"

    STATUS_CHOICES = [
        (STATUS_PRESENT, "Present"),
        (STATUS_ABSENT, "Absent"),
        (STATUS_LATE, "Late"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )

    class Meta:
        ordering = ["-date", "student__first_name"]

        # Q30: Prevent duplicate attendance for the same student and date.
        constraints = [
            models.UniqueConstraint(
                fields=["student", "date"],
                name="unique_student_attendance_per_day",
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"


# Q43: Certificate model
class Certificate(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    date_issued = models.DateField()

    class Meta:
        ordering = ["-date_issued"]
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_certificate_per_student_course",
            )
        ]

    def clean(self):
        if self.student_id and self.course_id:
            is_enrolled = self.student.courses.filter(
                pk=self.course_id,
            ).exists()
            if not is_enrolled:
                raise ValidationError(
                    "The student is not enrolled in this course."
                )

    def __str__(self):
        return f"{self.student} - {self.course}"
