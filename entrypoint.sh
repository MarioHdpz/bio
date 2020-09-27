#!/bin/sh

set -e

wait_for_db() {
    if [ -z "$POSTGRES_HOST" ] || [ -z "$POSTGRES_PORT" ]; then
        echo "No django database host or port, not waiting for db."
    else
        echo "Waiting for database"
        dockerize -wait tcp://"$POSTGRES_HOST":"$POSTGRES_PORT" -timeout 30s
    fi
}

wait_for_db

echo "Running migrations"
# Apply database migrations
python manage.py migrate

# Collect static files
echo "Running collectstatic"
python manage.py collectstatic --noinput

# Collect static files
# echo "Compile language messages"
# python manage.py compilemessages

exec "$@"
