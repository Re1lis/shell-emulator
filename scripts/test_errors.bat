@echo off
chcp 65001 >nul
cd /d "%~dp0.."
echo === 1. Скрипт с ошибочными строками ===
python src\main.py --vfs vfs\test.zip --script scripts\errors.txt
echo === 2. Несуществующий скрипт ===
python src\main.py --script scripts\net_takogo.txt
echo === 3. Без параметров (закрой окно вручную) ===
python src\main.py
pause
