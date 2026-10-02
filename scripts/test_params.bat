@echo off
chcp 65001 >nul
cd /d "%~dp0.."
echo === 1. Без параметров (закрой окно вручную) ===
python src\main.py
echo === 2. Только --vfs ===
python src\main.py --vfs vfs\test.zip
echo === 3. Только --script ===
python src\main.py --script scripts\demo.txt
echo === 4. Оба параметра ===
python src\main.py --vfs vfs\test.zip --script scripts\demo.txt
pause
