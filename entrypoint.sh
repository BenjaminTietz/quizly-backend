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

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn quizzly_backend.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --timeout 120
