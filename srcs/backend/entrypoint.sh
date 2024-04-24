#!/bin/sh

# Wait for the PostgreSQL server to be available
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start your Django app
exec "$@"