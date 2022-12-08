#!/bin/sh
cd ..

export LOGIN_TOKEN=dev
export USE_LIVE_SERVER=false

/usr/local/bin/python3.9 -m toontown.launcher.QuickStartLauncher
