#!/bin/sh
set -e

echo "🚀 Starting Quizly Backend"

if [ -n "$POSTGRES_HOST" ]; then
  echo "Waiting for PostgreSQL..."
  until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
    sleep 1
  done
  echo "✅ PostgreSQL is available"
fi

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating superuser if not exists..."

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME")
email = os.getenv("DJANGO_SUPERUSER_EMAIL")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("Superuser created")
    else:
        print("Superuser already exists")
else:
    print("Superuser env vars not set, skipping")
EOF


echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn quizzly_backend.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --timeout 120
