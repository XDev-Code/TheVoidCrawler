@echo off
cls
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python
    goto install
)
py --version >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=py
    goto install
)
echo Python is NOT installed or not in PATH.
echo Please install Python from https://python.org
pause
exit
:install
echo Installing requirements...
%PYTHON% -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements.
    pause
    exit
)
cls
start cmd.exe /k %PYTHON% main.py