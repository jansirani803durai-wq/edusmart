#!/usr/bin/env bash
# Q56-Q59: Render build commands
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
