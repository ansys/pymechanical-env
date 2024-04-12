@echo off
if "%OS%"=="Windows_NT" (
    echo This script is intended for Linux environments only.
    echo Use without `mechanical-env` if you are using Windows
    exit /b 1
)
bash mechanical-env.sh %*
