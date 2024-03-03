@echo off
title Toontown Modifications - Server Launcher
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH


set /P LOGIN_TOKEN="Username (default: dev): " || ^
set LOGIN_TOKEN=dev

set /P GAME_SERVER="Game Server (default: 127.0.0.1): " || ^
set GAME_SERVER=127.0.0.1

set USE_LIVE_SERVER=false
:main
%PPYTHON_PATH% -m toontown.launcher.QuickStartLauncher
pause
goto :main
