#!/bin/sh

cd /home/dmoseley/RpiDev-CrossPy
LAUNCH_CMD="python3 -Xfrozen_modules=off -m debugpy --listen 192.168.17.79:5678 --wait-for-client main.py"
echo "Starting debugpy server..."
pkill -f "${LAUNCH_CMD}"
${LAUNCH_CMD} &