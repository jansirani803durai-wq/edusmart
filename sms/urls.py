# Q17, Q28 and certificate/report routes
from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    # Q17: Student registration URL
    path(
        "students/register/",
        views.register_student,
        name="register_student",
    ),
    path(
        "students/",
        views.student_list,
        name="student_list",
    ),
    path(
        "students/<int:student_id>/",
        views.student_detail,
        name="student_detail",
    ),
    path(
        "students/<int:student_id>/attendance/",
        views.student_attendance_report,
        name="student_attendance_report",
    ),
    path(
        "students/<int:student_id>/courses/"
        "<int:course_id>/certificate/",
        views.issue_certificate,
        name="issue_certificate",
    ),
    path(
        "batches/",
        views.batch_list,
        name="batch_list",
    ),
    path(
        "batches/create/",
        views.create_batch,
        name="create_batch",
    ),

    # Q28: Dynamic batch attendance URL
    path(
        "batches/<int:batch_id>/attendance/",
        views.take_attendance,
        name="take_attendance",
    ),
    path(
        "batches/<int:batch_id>/attendance/report/",
        views.attendance_report,
        name="attendance_report",
    ),
    path(
        "courses/",
        views.course_list,
        name="course_list",
    ),
    path(
        "courses/create/",
        views.create_course,
        name="create_course",
    ),
]
