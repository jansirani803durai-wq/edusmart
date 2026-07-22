# EduTrack SMS — Q1 to Q60 Step-by-Step Code Map

Every question number is mapped to the exact source file. Code in the project is formatted across multiple lines for screenshots.

## Q1
Create and activate virtual environment — see README.md commands.

## Q2
Install Django and dependencies — requirements.txt.

## Q3
Create Django project edutrack — edutrack/ and manage.py.

## Q4
Create sms app — sms/ directory.

## Q5
Register sms app — edutrack/settings.py.

## Q6
Batch model — sms/models.py.

## Q7
Student model — sms/models.py.

## Q8
Attendance model — sms/models.py.

## Q9
Register all models in admin — sms/admin.py.

## Q10
Create/apply migrations — sms/migrations/0001_initial.py and README.md.

## Q11
StudentForm — sms/forms.py.

## Q12
register_student view — sms/views.py.

## Q13
GET request handling — sms/views.py register_student.

## Q14
POST validation — sms/views.py register_student.

## Q15
Save and redirect — sms/views.py register_student.

## Q16
Registration template — sms/templates/sms/register_student.html.

## Q17
Registration URL — sms/urls.py.

## Q18
Student list view — sms/views.py.

## Q19
Student list template — sms/templates/sms/student_list.html.

## Q20
Run and test server — README.md.

## Q21
AttendanceForm — sms/forms.py.

## Q22
take_attendance view — sms/views.py.

## Q23
Fetch batch students — sms/views.py.

## Q24
Render GET attendance page — sms/views.py.

## Q25
Attendance template — sms/templates/sms/take_attendance.html.

## Q26
Read status values from POST — sms/views.py.

## Q27
Save records using bulk_create — sms/views.py.

## Q28
Dynamic attendance URL — sms/urls.py.

## Q29
Batch attendance links — sms/templates/sms/batch_list.html.

## Q30
Duplicate prevention — sms/models.py and sms/views.py.

## Q31
attendance_report view — sms/views.py.

## Q32
Fetch report data — sms/views.py.

## Q33
Present/Absent/Late aggregation — sms/views.py.

## Q34
Report template — sms/templates/sms/attendance_report.html.

## Q35
Display report table — attendance_report.html.

## Q36
Individual report view — sms/views.py.

## Q37
Individual report link — student_list.html.

## Q38
Attendance history template — student_attendance_report.html.

## Q39
Attendance test procedure — SCREENSHOT_GUIDE_Q1_Q60.md.

## Q40
Professional responsive CSS — sms/static/sms/style.css.

## Q41
Course model — sms/models.py.

## Q42
Student-course ManyToMany — sms/models.py.

## Q43
Certificate model — sms/models.py.

## Q44
Course/certificate migration — sms/migrations/0001_initial.py.

## Q45
issue_certificate view — sms/views.py.

## Q46
ReportLab dependency — requirements.txt.

## Q47
Fetch student/course — sms/views.py.

## Q48
get_or_create certificate — sms/views.py.

## Q49
Create PDF canvas — sms/views.py.

## Q50
Certificate design — sms/views.py.

## Q51
Return FileResponse — sms/views.py.

## Q52
Issue Certificate button — student_detail.html.

## Q53
Unit tests — sms/tests.py.

## Q54
Run tests — README.md.

## Q55
Production environment settings — edutrack/settings.py.

## Q56
Static files and collectstatic — settings.py/build.sh.

## Q57
requirements.txt — project root.

## Q58
Gunicorn installation — requirements.txt.

## Q59
Gunicorn start command — Procfile/render.yaml.

## Q60
Dockerfile and docker-compose.yml — project root.
