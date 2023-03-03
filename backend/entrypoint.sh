#!/bin/sh
echo "Waiting for postgres..."

while ! nc -z kalya-db 5432; do
  sleep 0.1
done

echo "PostgreSQL of KalyaDB started"
exec "$@"