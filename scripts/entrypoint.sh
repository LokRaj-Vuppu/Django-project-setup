#!/bin/sh

set -e

# collecting static files
python manage.py collectstatic --noinput

# migrations
python manage.py makemigrations
python manage.py migrate


# python manage.py migrate django_celery_results


uwsgi --socket :8000 --master --enable-thread --module app.wsgi