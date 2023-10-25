@echo off
title SkyClub
color b
python -m pip show highrise-bot-sdk >nul 2>&1
if errorlevel 1 (
    echo Highrise SDK not found. Installing...
    python -m pip install highrise-bot-sdk
) else (
    echo Starting bot...
)
:loop
python main.py
echo nous attendons 3 seconde avant le redémarrage
timeout /t 3 /nobreak >nul
goto loop
