@echo off
if "%OS%"=="Windows_NT" (
    echo This script is intended for Linux environments only.
    echo Use without `mechanical-env` if you are using Windows
    echo For more information:
    echo https://mechanical.docs.pyansys.com/version/stable/getting_started/running_mechanical.html#embed-a-mechanical-instance
    exit /b 1
)
