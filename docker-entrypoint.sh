#!/bin/sh
python /opt/tester/tester.py &

exec "$@"
