@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (set "PYTHON=python") else (set "PYTHON=py -3")
if not exist ".venv\Scripts\python.exe" (
    %PYTHON% -m venv .venv
    if errorlevel 1 goto fail
)
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto fail
".venv\Scripts\python.exe" test_dashboard_logic.py
if errorlevel 1 goto fail
".venv\Scripts\python.exe" -m streamlit run app.py
if errorlevel 1 goto fail
exit /b 0
:fail
echo Setup or launch failed. Read the error above and check the README.
pause
exit /b 1
