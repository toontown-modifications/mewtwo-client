@echo off
title Open Toontown - Game Client
cd..

echo Warning!
echo This is for the Sunrise Games project.
echo Make an account here https://toontastic.sunrise.games/

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH



:main
%PPYTHON_PATH% -m launcher
pause
goto :main
