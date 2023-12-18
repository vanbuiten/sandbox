#!/usr/bin/env bash
set -eux

# Run migrations
alembic upgrade head

exec "$@"
