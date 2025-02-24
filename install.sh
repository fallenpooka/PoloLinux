@echo off
cd utils
start /B setup.vbs
cd ..
echo once done installing run polo.py
echo installing...
pip install -r requirements.txt

if %ERRORLEVEL% equ 0 (
    echo INstalled...
) else (
    echo Error...
)
pause
