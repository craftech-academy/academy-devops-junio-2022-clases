#!/bin/sh
python manage.py makemigrations
python manage.py flush --no-input
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py runserver 0.0.0.0:8001

exec "$@"