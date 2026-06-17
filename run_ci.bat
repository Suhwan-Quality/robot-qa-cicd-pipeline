@echo off

echo ================================
echo QA CI TEST START
echo ================================

if not exist reports mkdir reports
if not exist logs mkdir logs

echo [1/4] Install required packages
python -m pip install -r requirements.txt

echo [2/4] Save environment information
python --version > logs\environment_info.txt
python -m pip freeze >> logs\environment_info.txt

echo [3/4] Run automated tests
python -m pytest tests --junitxml=reports\result.xml --html=reports\result.html --self-contained-html > logs\test_log.txt

echo [4/4] Check Quality Gate
if %ERRORLEVEL% EQU 0 (
    echo [RESULT] TEST PASSED
    echo [QUALITY GATE] GO
    echo GO > reports\quality_gate.txt
    exit /b 0
) else (
    echo [RESULT] TEST FAILED
    echo [QUALITY GATE] NO-GO
    echo NO-GO > reports\quality_gate.txt
    exit /b 1
)