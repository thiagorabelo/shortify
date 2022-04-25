#!/bin/sh
set -e

WSGI_APP="shortify.wsgi:application"
BIND="${BIND:-0.0.0.0:8000}"
WORKERS="$(python -c 'import multiprocessing; print(multiprocessing.cpu_count() * 2 + 1)')"  # 2n+1
MAX_REQUESTS="${MAX_REQUESTS:-1000}"
MAX_REQUESTS_JITTER="${MAX_REQUESTS_JITTER:-30}"
LOG_LEVEL="${LOG_LEVEL:-info}"
LOG_FILE="${LOG_FILE:--}"
TIMEOUT="${TIMEOUT:-15}"

exec gunicorn "${WSGI_APP}" --bind "${BIND}" \
  -w "${WORKERS}" --max-requests="${MAX_REQUESTS}" \
  --max-requests-jitter="${MAX_REQUESTS_JITTER}" \
  --log-level="${LOG_LEVEL}" \
  --log-file="${LOG_FILE}" --timeout="${TIMEOUT}"
