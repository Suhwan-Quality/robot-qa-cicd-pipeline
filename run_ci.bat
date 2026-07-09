@echo off
setlocal

echo ==============================
echo QA CI TEST START
echo ==============================

if not exist reports mkdir reports
if not exist logs mkdir logs

echo [1/6] Install required packages
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
    echo [RESULT] PACKAGE INSTALL FAILED
    echo [QUALITY GATE] NO-GO
    echo NO-GO > reports\quality_gate.txt
    exit /b 1
)

echo [2/6] Save environment information
.\.venv\Scripts\python.exe --version > logs\environment_info.txt
.\.venv\Scripts\python.exe -m pip freeze >> logs\environment_info.txt

echo [3/6] Run Smoke Tests
.\.venv\Scripts\python.exe -m pytest tests\smoke -v --junitxml=reports\smoke_result.xml --html=reports\smoke_result.html --self-contained-html > logs\smoke_test_log.txt
if errorlevel 1 (
    echo [RESULT] SMOKE TEST FAILED
    echo [QUALITY GATE] NO-GO
    echo NO-GO > reports\quality_gate.txt
    exit /b 1
)

echo [4/6] Run Regression Tests
.\.venv\Scripts\python.exe -m pytest tests\regression -v --junitxml=reports\regression_result.xml --html=reports\regression_result.html --self-contained-html > logs\regression_test_log.txt
if errorlevel 1 (
    echo [RESULT] REGRESSION TEST FAILED
    echo [QUALITY GATE] NO-GO
    echo NO-GO > reports\quality_gate.txt
    exit /b 1
)

echo [5/6] Run Coverage Check
.\.venv\Scripts\python.exe -m pytest tests -v --cov=app.device --cov-report=term-missing --cov-report=xml:reports/coverage.xml --cov-report=html:reports/coverage_html --cov-fail-under=90 > logs\coverage_test_log.txt
if errorlevel 1 (
    echo [RESULT] COVERAGE CHECK FAILED
    echo [QUALITY GATE] NO-GO
    echo NO-GO > reports\quality_gate.txt
    exit /b 1
)

echo [6/6] Check Quality Gate
(
echo Quality Gate Result
echo -------------------
echo Smoke Test: PASS
echo Regression Test: PASS
echo Coverage Threshold: 90%%
echo Coverage Result: PASS
echo Quality Gate: GO
) > reports\quality_gate.txt

echo [RESULT] ALL TESTS PASSED
echo [QUALITY GATE] GO

endlocal