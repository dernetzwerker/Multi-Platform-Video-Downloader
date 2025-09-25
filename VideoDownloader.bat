@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul 2>&1
title Multi Platform Video Downloader  - dernetzwerker
color 0B

echo.
echo ################################################################
echo #                                                                                                                             #
echo #              MULTI PLATFORM VIDEO DOWNLOADER                                       #
echo #                                                                                                                             #
echo #           Downloads directly to desktop as numbered files                                   #
echo #                                                                                                                            #
echo #                GitHub: github.com/dernetzwerker                                                     #
echo #                                                                                                                            #
echo ################################################################
echo.

echo [INIT] Starting final version...
timeout /t 2 /nobreak >nul

:: Python detection
echo [CHECK] Searching for Python...
set PYTHON_FOUND=0
set PYTHON_CMD=

python --version >nul 2>&1
if !errorlevel! equ 0 (
    echo [FOUND] Python via 'python' command
    python --version
    set PYTHON_CMD=python
    set PYTHON_FOUND=1
    goto :SETUP_PACKAGES
)

py --version >nul 2>&1
if !errorlevel! equ 0 (
    echo [FOUND] Python via 'py' launcher  
    py --version
    set PYTHON_CMD=py
    set PYTHON_FOUND=1
    goto :SETUP_PACKAGES
)

python3 --version >nul 2>&1
if !errorlevel! equ 0 (
    echo [FOUND] Python via 'python3' command
    python3 --version
    set PYTHON_CMD=python3
    set PYTHON_FOUND=1
    goto :SETUP_PACKAGES
)

:: Auto-installation
echo [ERROR] Python not detected!
echo [AUTO] Installing Python...

winget --version >nul 2>&1
if !errorlevel! equ 0 (
    echo [WINGET] Installing Python 3.12...
    winget install Python.Python.3.12 --accept-source-agreements --accept-package-agreements --silent
    
    timeout /t 8 /nobreak >nul
    
    python --version >nul 2>&1
    if !errorlevel! equ 0 (
        set PYTHON_CMD=python
        set PYTHON_FOUND=1
        echo [SUCCESS] Python installation successful!
        goto :SETUP_PACKAGES
    )
)

echo [MANUAL] Please install Python manually:
echo [1] Microsoft Store - Search "Python 3.12"
echo [2] Python.org - Download from official site
echo.
set /p choice="Open installation source? [1/2/n]: "

if "!choice!"=="1" start ms-windows-store://search/?query=python 3.12
if "!choice!"=="2" start https://python.org/downloads

echo After installation, restart this program.
goto :WAIT_EXIT

:SETUP_PACKAGES
echo.
echo [SETUP] Using Python: !PYTHON_CMD!
echo [INFO] Installing packages...

!PYTHON_CMD! -m pip install --upgrade pip --quiet
!PYTHON_CMD! -m pip install yt-dlp --upgrade --quiet

if not exist "video_downloader_final.py" (
    echo [ERROR] Main file 'video_downloader_final.py' not found!
    goto :WAIT_EXIT
)

echo [START] Launching final video downloader...
echo [USER] dernetzwerker
echo [TIME] %DATE% %TIME%
echo.

!PYTHON_CMD! video_downloader_final.py

:WAIT_EXIT
echo.
echo ################################################################
echo #                                                                                                                            #
echo #                     FEATURES                                                                                    #
echo #                                                                                                                            #
echo #  [+] Downloads directly to desktop                                                                    #
echo #  [+] Numbered files: download1.mp4, download2.mp3                                    #
echo #  [+] No folder creation                                                                                       #
echo #                                                                                                                          #
echo ################################################################
echo.

echo Press any key to close window...
pause >nul
exit /b 0