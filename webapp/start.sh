#! /usr/bin/env sh
set -e

# Start Supervisor, with Nginx and uWSGI
exec /usr/bin/supervisord
