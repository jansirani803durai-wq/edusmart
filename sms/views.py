# ------------------------------------------
# Q11 - Import Required Modules
# ------------------------------------------
import io
from datetime import date

from django.contrib import messages
from django.db import transaction
from django.db.models import Count, Q
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from .forms import StudentForm, BatchForm, CourseForm
from .models import Student, Batch, Attendance, Course, Certificate


# ------------------------------------------
# Q20 - Dashboard
# ------------------------------------------
def home(request):
    return render(
        request,
        "sms/home.html",
        {
            "student_count": Student.objects.count(),
            "batch_count": Batch.objects.count(),
            "course_count": Course.objects.count(),
            "attendance_count": Attendance.objects.count(),
        },
    )


# ------------------------------------------
# Q12 - Register Student View
# Q13 - Handle GET Request
# Q14 - Handle POST Request
# Q15 - Save Student
# ------------------------------------------
def register_student(request):
    form = StudentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student registered successfully.")
        return redirect("student_list")

    return render(request, "sms/register_student.html", {"form": form})


# ------------------------------------------
# Q18 - Student List
# ------------------------------------------
def student_list(request):
    return render(
        request,
        "sms/student_list.html",
        {
            "students": Student.objects.select_related("batch")
            .prefetch_related("courses")
        },
    )


# ------------------------------------------
# Q19 - Student Details
# ------------------------------------------
def student_detail(request, student_id):
    return render(
        request,
        "sms/student_detail.html",
        {
            "student": get_object_or_404(
                Student.objects.prefetch_related("courses"),
                pk=student_id,
            )
        },
    )


# ------------------------------------------
# Q29 - Batch List
# ------------------------------------------
def batch_list(request):
    return render(
        request,
        "sms/batch_list.html",
        {
            "batches": Batch.objects.annotate(
                student_total=Count("students")
            )
        },
    )


# ------------------------------------------
# Q6 - Create Batch
# ------------------------------------------
def create_batch(request):
    form = BatchForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("batch_list")

    return render(
        request,
        "sms/simple_form.html",
        {
            "form": form,
            "title": "Create Batch",
        },
    )


# ------------------------------------------
# Q41 - Course List
# ------------------------------------------
def course_list(request):
    return render(
        request,
        "sms/course_list.html",
        {"courses": Course.objects.all()},
    )


# ------------------------------------------
# Q41 - Create Course
# ------------------------------------------
def create_course(request):
    form = CourseForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("course_list")

    return render(
        request,
        "sms/simple_form.html",
        {
            "form": form,
            "title": "Create Course",
        },
    )


# ------------------------------------------
# Q22 - Take Attendance View
# Q23 - Fetch Students
# Q24 - Handle GET
# Q26 - Handle POST
# Q27 - Save Attendance
# Q30 - Prevent Duplicate Attendance
# ------------------------------------------
def take_attendance(request, batch_id):

    batch = get_object_or_404(Batch, pk=batch_id)

    students = batch.students.all()

    d = (
        request.POST.get("attendance_date")
        or request.GET.get("date")
    )

    try:
        attendance_date = (
            date.fromisoformat(d)
            if d
            else date.today()
        )
    except ValueError:
        attendance_date = date.today()

    exists = Attendance.objects.filter(
        student__batch=batch,
        date=attendance_date,
    ).exists()

    if request.method == "POST":

        if exists:
            messages.error(
                request,
                "Attendance already recorded for this batch and date.",
            )
            return redirect(
                "take_attendance",
                batch_id=batch.id,
            )

        valid = {
            x[0]
            for x in Attendance.STATUS_CHOICES
        }

        records = []

        for s in students:

            status = request.POST.get(
                f"status_{s.id}"
            )

            if status not in valid:
                messages.error(
                    request,
                    f"Select status for {s.full_name}.",
                )
                return redirect(
                    "take_attendance",
                    batch_id=batch.id,
                )

            records.append(
                Attendance(
                    student=s,
                    date=attendance_date,
                    status=status,
                )
            )

        with transaction.atomic():
            Attendance.objects.bulk_create(records)

        messages.success(
            request,
            "Attendance saved successfully.",
        )

        return redirect(
            "attendance_report",
            batch_id=batch.id,
        )

    return render(
        request,
        "sms/take_attendance.html",
        {
            "batch": batch,
            "students": students,
            "attendance_date": attendance_date,
            "already_recorded": exists,
            "status_choices": Attendance.STATUS_CHOICES,
        },
    )


# ------------------------------------------
# Q31
# Q32
# Q33
# Q35
# ------------------------------------------
def attendance_report(request, batch_id):

    batch = get_object_or_404(
        Batch,
        pk=batch_id,
    )

    students = batch.students.annotate(

        present_count=Count(
            "attendance_records",
            filter=Q(
                attendance_records__status="Present"
            ),
        ),

        absent_count=Count(
            "attendance_records",
            filter=Q(
                attendance_records__status="Absent"
            ),
        ),

        late_count=Count(
            "attendance_records",
            filter=Q(
                attendance_records__status="Late"
            ),
        ),
    )

    return render(
        request,
        "sms/attendance_report.html",
        {
            "batch": batch,
            "students": students,
        },
    )


# ------------------------------------------
# Q36
# Q38
# ------------------------------------------
def student_attendance_report(
    request,
    student_id,
):

    student = get_object_or_404(
        Student,
        pk=student_id,
    )

    records = student.attendance_records.all()

    summary = records.aggregate(

        present=Count(
            "id",
            filter=Q(status="Present"),
        ),

        absent=Count(
            "id",
            filter=Q(status="Absent"),
        ),

        late=Count(
            "id",
            filter=Q(status="Late"),
        ),
    )

    return render(
        request,
        "sms/student_attendance_report.html",
        {
            "student": student,
            "records": records,
            "summary": summary,
        },
    )


# ------------------------------------------
# Q45
# Q47
# Q48
# Q49
# Q50
# Q51
# ------------------------------------------
def issue_certificate(
    request,
    student_id,
    course_id,
):
 #que 47
    student = get_object_or_404(
        Student,
        pk=student_id,
    )

    course = get_object_or_404(
        Course,
        pk=course_id,
    )

    if not student.courses.filter(
        pk=course.id
    ).exists():
        raise Http404(
            "Student is not enrolled in this course."
        )

    cert, _ = Certificate.objects.get_or_create(
        student=student,
        course=course,
        defaults={
            "date_issued": date.today(),
        },
    )

    b = io.BytesIO()

    width, height = landscape(A4)

    pdf = canvas.Canvas(
        b,
        pagesize=landscape(A4),
    )

    pdf.setStrokeColor(colors.HexColor("#1f4e78"))
    pdf.setLineWidth(5)

    pdf.rect(
        1.2 * cm,
        1.2 * cm,
        width - 2.4 * cm,
        height - 2.4 * cm,
    )

    pdf.setFont("Helvetica-Bold", 28)

    pdf.drawCentredString(
        width / 2,
        height - 4 * cm,
        "CERTIFICATE OF COMPLETION",
    )

    pdf.setFont("Helvetica", 15)

    pdf.drawCentredString(
        width / 2,
        height - 6 * cm,
        "This certificate is proudly presented to",
    )

    pdf.setFillColor(colors.HexColor("#8b6508"))

    pdf.setFont("Helvetica-Bold", 30)

    pdf.drawCentredString(
        width / 2,
        height - 8.2 * cm,
        student.full_name,
    )

    pdf.setFillColor(colors.black)

    pdf.setFont("Helvetica", 15)

    pdf.drawCentredString(
        width / 2,
        height - 10 * cm,
        "for successfully completing the course",
    )

    pdf.setFont("Helvetica-Bold", 23)

    pdf.drawCentredString(
        width / 2,
        height - 11.8 * cm,
        course.name,
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawCentredString(
        width / 2,
        3.4 * cm,
        f"Issued on {cert.date_issued.strftime('%d %B %Y')}",
    )

    pdf.save()

    b.seek(0)

    return FileResponse(
        b,
        as_attachment=True,
        filename=f"{student.full_name.replace(' ', '_')}_certificate.pdf",
    )