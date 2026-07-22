# EduTrack SMS — Day 83 to Day 85, Q1–Q60

This ZIP is already a complete Django project. **Do not run** `django-admin startproject edutrack` or `python manage.py startapp sms` again.

## Windows setup

```powershell
cd EduTrack_SMS_Q1_Q60_Question_Numbered_Render_Ready
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py test
python manage.py runserver
```

Open:

- App: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Question-numbered documentation

- `Q1_TO_Q60_STEP_BY_STEP_CODE.md`
- `QUESTION_WISE_GUIDE_Q1_Q60.md`
- `SCREENSHOT_GUIDE_Q1_Q60.md`

The primary Python files also contain comments such as `# Q6`, `# Q22-Q30`, and `# Q45-Q51`.

## Render deployment

This project includes Render Blueprint deployment with PostgreSQL.

1. Upload the complete extracted project to GitHub.
2. In Render, select **New → Blueprint**.
3. Connect the GitHub repository.
4. Render reads `render.yaml` and creates the web service and PostgreSQL database.
5. Deploy.

Manual Web Service settings:

- Build Command: `bash build.sh`
- Start Command: `gunicorn edutrack.wsgi:application`

Required environment variables when deploying manually:

```text
DEBUG=False
SECRET_KEY=<strong-random-key>
ALLOWED_HOSTS=<service-name>.onrender.com
CSRF_TRUSTED_ORIGINS=https://<service-name>.onrender.com
DATABASE_URL=<Render PostgreSQL internal database URL>
```

## Docker

```bash
docker compose up --build
```
