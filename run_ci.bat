@echo off

echo ================================
echo QA CI TEST START
echo ================================

if not exist reports mkdir reports
if not exist logs mkdir logs

echo [1/3] Install required packages
pip install -r requirements.txt

echo [2/3] Run automated tests
python -m pytest tests --junitxml=reports\result.xml --html=reports\result.html --self-contained-html > logs\test_log.txt

echo [3/3] Check test result
if %ERRORLEVEL% EQU 0 (
    echo [RESULT] TEST PASSED
    echo [QUALITY GATE] GO
    exit /b 0
) else (
    echo [RESULT] TEST FAILED
    echo [QUALITY GATE] NO-GO
    exit /b 1
)