@echo off

echo ================================
echo QA CI TEST START
echo ================================

if not exist reports mkdir reports
if not exist logs mkdir logs

echo [1/5] Install required packages
python -m pip install -r requirements.txt

echo [2/5] Save environment information
python --version > logs\environment_info.txt
python -m pip freeze >> logs\environment_info.txt

echo [3/5] Run Smoke Tests
python -m pytest tests\smoke --junitxml=reports\smoke_result.xml --html=reports\smoke_result.html --self-contained-html > logs\smoke_test_log.txt

if %ERRORLEVEL% NEQ 0 (
    echo [RESULT] SMOKE TEST FAILED
    echo [QUALITY GATE] NO-GO
    echo NO-GO > reports\quality_gate.txt
    exit /b 1
)

echo [4/5] Run Regression Tests
python -m pytest tests\regression --junitxml=reports\regression_result.xml --html=reports\regression_result.html --self-contained-html > logs\regression_test_log.txt

if %ERRORLEVEL% NEQ 0 (
    echo [RESULT] REGRESSION TEST FAILED
    echo [QUALITY GATE] NO-GO
    echo NO-GO > reports\quality_gate.txt
    exit /b 1
)

echo [5/5] Check Quality Gate
echo [RESULT] ALL TESTS PASSED
echo [QUALITY GATE] GO
echo GO > reports\quality_gate.txt
exit /b 0