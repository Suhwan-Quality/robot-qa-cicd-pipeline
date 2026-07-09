# CI/CD 기반 QA 자동화 검증 환경 구축 실습  
## Mock Robot Device Smoke & Regression Test Automation Project

[![QA CI Pipeline](https://github.com/Suhwan-Quality/robot-qa-cicd-pipeline/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Suhwan-Quality/robot-qa-cicd-pipeline/actions/workflows/ci.yml)

## 1. 프로젝트 개요

본 프로젝트는 로봇/임베디드 시스템 검증 업무에서 활용 가능한 CI/CD 기반 QA 자동화 검증 환경을 학습하고 구현하기 위한 개인 포트폴리오 프로젝트입니다.

실제 장비가 없는 환경을 가정하여 `Mock Robot Device`를 구성하고, Python `pytest` 기반으로 장비 연결, 버전 조회, 모터 상태, 비상정지 상태, 예외 명령 응답에 대한 자동화 테스트를 구성했습니다.

초기에는 단일 테스트 파일 기반으로 테스트를 수행했으며, 이후 실무형 구조에 맞춰 `Smoke Test`와 `Regression Test`를 분리했습니다.

본 프로젝트의 목적은 단순 테스트 코드 작성이 아니라, QA 관점에서 다음 흐름을 직접 구성하고 이해하는 것입니다.

```text
테스트 대상 정의
        ↓
테스트 케이스 설계
        ↓
Smoke / Regression Test 분리
        ↓
자동화 테스트 실행
        ↓
Pass / Fail 판정
        ↓
HTML / XML Report 생성
        ↓
Log / Environment Info 저장
        ↓
Quality Gate GO / NO-GO 판단
        ↓
GitHub Actions CI 자동 실행
        ↓
Artifact 저장 및 결과 검토
```

---

## 2. 프로젝트 목적

본 프로젝트의 목적은 다음과 같습니다.

* 수동 검증 항목을 자동화 테스트 케이스로 전환
* Python / pytest 기반 자동화 테스트 구조 이해
* Mock Device를 활용한 로봇/장비 검증 시나리오 구성
* Smoke Test와 Regression Test 목적 분리
* JUnit XML Report 및 HTML Test Report 생성
* 테스트 실행 로그 및 환경 정보 저장
* `run_ci.bat` 기반 Local CI Pipeline 구성
* GitHub Actions 기반 CI Workflow 구성
* 테스트 결과 기반 Quality Gate GO / NO-GO 판단 흐름 구현
* CI 실패 로그 분석 및 Troubleshooting 경험 확보

---

## 3. 사용 기술

| Category          | Tool / Technology                                   |
| ----------------- | --------------------------------------------------- |
| Language          | Python                                              |
| Test Framework    | pytest                                              |
| Test Report       | pytest-html, JUnit XML                              |
| Local Execution   | Windows PowerShell, Batch Script                    |
| Version Control   | Git                                                 |
| Remote Repository | GitHub                                              |
| CI Tool           | GitHub Actions                                      |
| Artifact          | HTML Report, XML Report, Test Log, Environment Info |
| Quality Gate      | GO / NO-GO text result                              |

---

## 4. 프로젝트 구조

```text
qa-cicd-practice/
 ├─ app/
 │   ├─ __init__.py
 │   ├─ device.py
 │   └─ python_basic_study/
 │       ├─ 01_python_basic.py
 │       ├─ 02_function_basic.py
 │       ├─ 03_list_dict_basic.py
 │       ├─ 04_test_case_loop_basic.py
 │       ├─ 05_test_result_summary_basic.py
 │       └─ 06_quality_gate_basic.py
 │
 ├─ tests/
 │   ├─ __init__.py
 │   ├─ smoke/
 │   │   └─ test_device_smoke.py
 │   └─ regression/
 │       └─ test_device_regression.py
 │
 ├─ reports/
 │   ├─ smoke_result.xml
 │   ├─ smoke_result.html
 │   ├─ regression_result.xml
 │   ├─ regression_result.html
 │   ├─ quality_gate.txt
 │   └─ quality_gate_basic.txt
 │
 ├─ logs/
 │   ├─ smoke_test_log.txt
 │   ├─ regression_test_log.txt
 │   └─ environment_info.txt
 │
 ├─ .github/
 │   └─ workflows/
 │       └─ ci.yml
 │
 ├─ requirements.txt
 ├─ run_ci.bat
 ├─ .gitignore
 └─ README.md
```

---

## 5. 테스트 대상

테스트 대상은 실제 로봇 장비가 아닌 `Mock Robot Device`입니다.

실제 장비가 없는 환경에서도 QA 자동화 테스트 구조를 학습하기 위해 가상의 장비 객체를 만들고, 해당 장비의 기본 동작과 예외 응답을 검증하도록 구성했습니다.

Mock Device는 다음 기능을 제공합니다.

* 장비 연결
* SW 버전 조회
* 모터 상태 조회
* 비상정지 상태 조회
* 명령어 응답 처리
* 비정상 명령 예외 응답 처리
* 미연결 상태에서의 Error 응답 처리

---

## 6. Mock Device 코드 개념

`app/device.py` 파일에는 테스트 대상이 되는 `MockRobotDevice`가 정의되어 있습니다.

QA 관점에서 이 코드는 실제 장비 또는 서버 API를 대신하는 테스트 대상입니다.

예를 들어 실제 업무에서는 다음과 같은 대상과 연결될 수 있습니다.

```text
실제 로봇 제어기
서버 API
장비 제어 SW
임베디드 보드
시뮬레이터
테스트용 Stub Server
```

본 프로젝트에서는 학습 목적상 실제 장비 대신 Mock Device를 사용했습니다.

---

## 7. Python 테스트 코드 기본 개념

본 프로젝트의 테스트 코드는 Python과 pytest를 사용합니다.

예시:

```python
from app.device import MockRobotDevice


def test_device_connection():
    device = MockRobotDevice()

    result = device.connect()

    assert result == "CONNECTED"
```

각 코드의 의미는 다음과 같습니다.

| Code                                     | Meaning                                             |
| ---------------------------------------- | --------------------------------------------------- |
| `from app.device import MockRobotDevice` | 테스트 대상 Mock Device를 불러옴                             |
| `device = MockRobotDevice()`             | 테스트 대상 장비 객체 생성                                     |
| `result = device.connect()`              | 테스트 Step 실행                                         |
| `assert result == "CONNECTED"`           | Expected Result와 Actual Result를 비교하여 Pass / Fail 판정 |

QA 문서 관점으로 보면 다음과 같습니다.

```text
Test Step:
- Device Connect 수행

Expected Result:
- CONNECTED 응답 반환

Actual Result:
- result 값 확인

Pass / Fail:
- Expected Result와 Actual Result가 일치하면 Pass
- 다르면 Fail
```

즉, Python의 `assert`는 QA 테스트 케이스의 Pass / Fail 판정 기준 역할을 합니다.

---

## 8. Smoke Test

Smoke Test는 빌드가 기본적으로 검증 가능한 상태인지 빠르게 판단하기 위한 테스트입니다.

본 프로젝트에서는 다음 항목을 Smoke Test로 구성했습니다.

```text
1. Device Connection Test
2. Version Read Test
3. Motor Status READY Test
4. Emergency Stop Default Status Test
```

Smoke Test 파일 위치:

```text
tests/smoke/test_device_smoke.py
```

Smoke Test 구성:

| Test Case                            | Description                 | QA Meaning        |
| ------------------------------------ | --------------------------- | ----------------- |
| `test_device_connection`             | Mock Robot Device 연결 상태 확인  | 장비 연결 가능 여부 확인    |
| `test_read_version_after_connection` | 연결 후 SW Version 정상 조회 확인    | SW 버전 확인 가능 여부 검증 |
| `test_motor_status_is_ready`         | Motor Status가 READY 상태인지 확인 | 기본 구동 준비 상태 확인    |
| `test_emergency_stop_is_false`       | E-Stop 기본 상태가 False인지 확인    | 비상정지 상태 기본값 확인    |

Smoke Test가 실패하면 시스템이 기본 검증 가능한 상태가 아니라고 판단할 수 있습니다.

따라서 실제 CI 환경에서는 Smoke Test 실패 시 이후 Regression Test를 수행하지 않고 Quality Gate를 NO-GO로 판단하는 구조로 확장할 수 있습니다.

---

## 9. Regression Test

Regression Test는 기존 기능 및 예외처리 동작이 수정 후에도 유지되는지 확인하기 위한 테스트입니다.

본 프로젝트에서는 다음 항목을 Regression Test로 구성했습니다.

```text
1. Invalid Command Error Response Test
2. Read Version Without Connection Test
3. Motor Status Without Connection Test
4. Emergency Stop Status Without Connection Test
```

Regression Test 파일 위치:

```text
tests/regression/test_device_regression.py
```

Regression Test 구성:

| Test Case                                       | Description                             | QA Meaning          |
| ----------------------------------------------- | --------------------------------------- | ------------------- |
| `test_invalid_command_returns_error`            | 비정상 명령 입력 시 Error Code 반환 확인            | 잘못된 명령에 대한 예외처리 검증  |
| `test_read_version_without_connection`          | 미연결 상태에서 Version 조회 시 Error 반환 확인       | 연결 전 기능 호출 방어 로직 검증 |
| `test_motor_status_without_connection`          | 미연결 상태에서 Motor Status 조회 시 Error 반환 확인  | 미연결 상태 예외처리 검증      |
| `test_emergency_stop_status_without_connection` | 미연결 상태에서 E-Stop Status 조회 시 Error 반환 확인 | 미연결 상태 안전 응답 검증     |

Regression Test는 수정 또는 기능 변경 이후 기존 예외처리 로직이 깨지지 않았는지 확인하기 위한 회귀 검증 목적으로 구성했습니다.

## 9-1. Parameterized Test & Shared Fixture Refactoring

Day 2에서는 `pytest.mark.parametrize`를 활용하여 동일한 검증 로직을 여러 조건 데이터로 반복 실행할 수 있도록 테스트 구조를 개선했습니다.

또한 테스트 파일 내부에 중복으로 정의되어 있던 fixture를 제거하고, `tests/conftest.py`에 정의된 공통 fixture를 사용하도록 정리했습니다.

이를 통해 테스트 준비 코드와 실제 검증 로직을 분리하고, 테스트 코드의 재사용성과 유지보수성을 개선했습니다.

---

### Updated Test Structure

```text
tests/
 ├─ conftest.py
 │   └─ Common robot_device fixture
 │
 ├─ test_parametrize_robot_device.py
 │   └─ Parameterized motor status validation
 │
 ├─ smoke/
 │   └─ test_device_smoke.py
 │
 └─ regression/
     └─ test_device_regression.py
```

---

### Test Scenario

| Test Condition | Expected Result | QA Meaning |
|---|---|---|
| Device is not connected | `ERROR_NOT_CONNECTED` | 미연결 상태에서 모터 상태 조회 시 예외 응답 확인 |
| Device is connected | `READY` | 연결 상태에서 모터 상태가 정상 준비 상태인지 확인 |

---

### Implemented Test

```python
@pytest.mark.parametrize(
    "should_connect, expected_status",
    [
        (False, "ERROR_NOT_CONNECTED"),
        (True, "READY"),
    ]
)
def test_motor_status_by_connection_state(robot_device, should_connect, expected_status):
    if should_connect:
        robot_device.connect()

    actual_status = robot_device.read_motor_status()

    assert actual_status == expected_status
```

---

### Validation Result

Parameterized test execution:

```powershell
.\.venv\Scripts\python.exe -m pytest .\tests\test_parametrize_robot_device.py -v
```

Result:

```text
2 passed
```

Full pytest execution:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Result:

```text
17 passed
```

Local CI execution:

```powershell
.\run_ci.bat
```

Result:

```text
[RESULT] ALL TESTS PASSED
[QUALITY GATE] GO
```

GitHub Actions result:

```text
Workflow: QA CI Pipeline
Job: qa-test
Status: Success
Total duration: 35s
Artifacts: 1
```

---

### QA Engineering Point

This update demonstrates a practical QA automation pattern where the same validation logic can be executed against multiple input conditions without duplicating test code.

By using a shared fixture from `conftest.py`, the test environment setup is centralized, while each test file focuses only on validation logic.

This structure improves:

- Test code maintainability
- Reusability of test setup
- Scalability for additional test conditions
- Regression test stability
- CI/CD pipeline integration quality

## 10. 설치 및 실행 방법

### 10-1. 프로젝트 폴더 이동

```bat
cd C:\qa-cicd-practice
```

---

### 10-2. 가상환경 생성

```bat
python -m venv .venv
```

---

### 10-3. 가상환경 활성화

```bat
.\.venv\Scripts\activate
```

정상적으로 활성화되면 PowerShell 앞에 다음과 같이 표시됩니다.

```text
(.venv) PS C:\qa-cicd-practice>
```

---

### 10-4. 필요 패키지 설치

```bat
python -m pip install -r requirements.txt
```

`requirements.txt` 내용:

```text
pytest
pytest-html
```

---

## 11. 테스트 실행 방법

### 11-1. 전체 테스트 실행

```bat
python -m pytest tests -v
```

정상 결과:

```text
17 passed
```

---

### 11-2. Smoke Test만 실행

```bat
python -m pytest tests\smoke -v
```

정상 결과:

```text
4 passed
```

---

### 11-3. Regression Test만 실행

```bat
python -m pytest tests\regression -v
```

정상 결과:

```text
4 passed
```

---

## 12. Report 생성 방법

### 12-1. Smoke Test Report 생성

```bat
python -m pytest tests\smoke --junitxml=reports\smoke_result.xml --html=reports\smoke_result.html --self-contained-html
```

생성 파일:

```text
reports/smoke_result.xml
reports/smoke_result.html
```

---

### 12-2. Regression Test Report 생성

```bat
python -m pytest tests\regression --junitxml=reports\regression_result.xml --html=reports\regression_result.html --self-contained-html
```

생성 파일:

```text
reports/regression_result.xml
reports/regression_result.html
```

---

## 13. Local CI Pipeline

본 프로젝트는 로컬 환경에서도 CI와 유사한 흐름으로 테스트를 실행할 수 있도록 `run_ci.bat` 파일을 구성했습니다.

Local CI Pipeline 실행 명령어:

```bat
.\run_ci.bat
```

`run_ci.bat` 실행 시 다음 순서로 테스트가 수행됩니다.

```text
1. Install required packages
2. Save environment information
3. Run Smoke Tests
4. Run Regression Tests
5. Check Quality Gate
```

정상 실행 결과:

```text
[1/5] Install required packages
[2/5] Save environment information
[3/5] Run Smoke Tests
[4/5] Run Regression Tests
[5/5] Check Quality Gate
[RESULT] ALL TESTS PASSED
[QUALITY GATE] GO
```

Local CI Pipeline 실행 후 다음 산출물이 생성됩니다.

```text
reports/
 ├─ smoke_result.html
 ├─ smoke_result.xml
 ├─ regression_result.html
 ├─ regression_result.xml
 └─ quality_gate.txt

logs/
 ├─ smoke_test_log.txt
 ├─ regression_test_log.txt
 └─ environment_info.txt
```

---

## 14. Quality Gate

Quality Gate는 테스트 결과를 기준으로 다음 단계 진행 여부를 판단하는 기준입니다.

본 프로젝트에서는 테스트 결과에 따라 `reports/quality_gate.txt` 파일에 다음 결과를 저장합니다.

```text
GO
```

또는:

```text
NO-GO
```

판정 기준은 다음과 같습니다.

| Condition                              | Quality Gate Result |
| -------------------------------------- | ------------------- |
| Smoke Test Pass + Regression Test Pass | GO                  |
| Smoke Test Fail                        | NO-GO               |
| Regression Test Fail                   | NO-GO               |

QA 관점에서 Quality Gate는 릴리즈 또는 다음 검증 단계 진행 여부를 판단하는 기준으로 활용할 수 있습니다.

---

## 14-1. Coverage-based Quality Gate Extension

Day 3에서는 기존 Quality Gate 기준을 확장하여, 테스트 통과 여부뿐 아니라 코드 커버리지 기준까지 함께 검증하도록 개선했습니다.

기존 Quality Gate는 Smoke Test와 Regression Test가 모두 통과하면 `GO`로 판단하는 구조였습니다.

Day 3에서는 여기에 `pytest-cov` 기반 Coverage Check를 추가하여, `app/device.py` 기준 코드 커버리지가 90% 이상일 때만 Quality Gate가 `GO`가 되도록 확장했습니다.

---

### Updated Quality Gate Criteria

| Condition | Quality Gate Result |
|---|---|
| Smoke Test PASS + Regression Test PASS + Coverage >= 90% | GO |
| Smoke Test FAIL | NO-GO |
| Regression Test FAIL | NO-GO |
| Coverage < 90% | NO-GO |

---

### Coverage Target

본 프로젝트에서는 학습용 Python 파일 전체가 아닌, 실제 테스트 대상 모듈인 `app/device.py`를 기준으로 Coverage를 측정했습니다.

```text
Coverage Target: app/device.py
Coverage Threshold: 90%
Actual Coverage: 93%
```

`app/python_basic_study/` 폴더는 Python 기초 학습용 코드이므로 Coverage 측정 대상에서 제외했습니다.

---

### Coverage Command

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v --cov=app.device --cov-report=term-missing --cov-report=xml:reports/coverage.xml
```

Command Meaning:

```text
.\.venv\Scripts\python.exe
→ 현재 프로젝트의 가상환경 Python을 사용한다.

-m pytest
→ Python에게 pytest 모듈을 실행하라고 지시한다.

tests
→ tests 폴더 안의 전체 테스트를 실행한다.

-v
→ 테스트 실행 결과를 자세히 출력한다.

--cov=app.device
→ app/device.py 파일 기준으로 코드 커버리지를 측정한다.

--cov-report=term-missing
→ 터미널에 커버리지 결과와 누락된 라인을 표시한다.

--cov-report=xml:reports/coverage.xml
→ coverage.xml 파일을 reports 폴더에 생성한다.
```

---

### Coverage Validation Result

Coverage 실행 결과 전체 테스트가 정상 통과했고, `app/device.py` 기준 93% Coverage를 확인했습니다.

```text
17 passed
app/device.py Coverage: 93%
Coverage XML written to reports/coverage.xml
```

Coverage Summary:

```text
Name           Stmts   Miss   Cover   Missing
---------------------------------------------
app/device.py    27      2     93%    29, 34
---------------------------------------------
TOTAL            27      2     93%
```

---

### Local CI Pipeline Update

`run_ci.bat`에 Coverage Check 단계를 추가하여, 로컬 CI에서도 Coverage 기준을 검증하도록 확장했습니다.

Updated Local CI Flow:

```text
1. Install required packages
2. Save environment information
3. Run Smoke Tests
4. Run Regression Tests
5. Run Coverage Check
6. Check Quality Gate
```

Local CI 실행 결과:

```text
[1/6] Install required packages
[2/6] Save environment information
[3/6] Run Smoke Tests
[4/6] Run Regression Tests
[5/6] Run Coverage Check
[6/6] Check Quality Gate
[RESULT] ALL TESTS PASSED
[QUALITY GATE] GO
```

---

### GitHub Actions CI Update

GitHub Actions Workflow에도 Coverage Check 단계를 추가했습니다.

이를 통해 GitHub에 코드가 push될 때마다 Smoke Test, Regression Test, Coverage Check가 자동으로 실행됩니다.

Updated GitHub Actions Flow:

```text
1. Source Code Checkout
2. Python 3.12 환경 구성
3. requirements.txt 기반 패키지 설치
4. reports / logs 폴더 생성
5. 환경 정보 저장
6. Smoke Test 실행
7. Regression Test 실행
8. Coverage Check 실행
9. Quality Gate 결과 저장
10. Artifact 업로드
```

GitHub Actions 실행 결과:

```text
Workflow: QA CI Pipeline
Job: qa-test
Status: Success
Total Duration: 35s
Artifacts: 1
```

---

### Coverage Artifacts

Coverage Check 실행 후 다음 산출물이 생성됩니다.

| Artifact | Description |
|---|---|
| `logs/coverage_test_log.txt` | Coverage Check 실행 로그 |
| `reports/coverage.xml` | CI 도구 연동용 XML Coverage Report |
| `reports/coverage_html/` | 사람이 확인 가능한 HTML Coverage Report |
| `reports/quality_gate.txt` | Smoke / Regression / Coverage 기준 기반 Quality Gate 결과 |

---

### QA Engineering Point

이번 개선을 통해 단순히 테스트가 통과했는지만 확인하는 구조에서 벗어나, 코드 커버리지라는 정량 기준을 Quality Gate에 반영했습니다.

QA 관점에서 의미는 다음과 같습니다.

- 테스트 통과 여부와 코드 커버리지 기준을 함께 검증
- Coverage 기준 미달 시 CI 실패 처리
- Quality Gate 기준을 정량화
- 테스트 결과, 로그, 커버리지 리포트를 Artifact로 보관
- 수동 검증 경험을 CI 기반 자동 품질 검증 흐름으로 확장

이를 통해 본 프로젝트는 단순 pytest 실행 예제가 아니라, Smoke / Regression / Coverage 기준을 포함한 CI Quality Gate 자동화 구조로 확장되었습니다.

---

## 15. Python 기초 기반 QA 검증 로직 및 Quality Gate 확장

본 프로젝트는 단순히 pytest와 GitHub Actions를 실행하는 것에서 끝나지 않고, Python 기초 문법을 기반으로 QA 검증 로직이 어떻게 구성되는지 단계적으로 확장했습니다.

목적은 Python 개발자 수준의 복잡한 구현이 아니라, QA 엔지니어 관점에서 테스트 데이터 관리, 기대값과 실제값 비교, PASS/FAIL 판정, Quality Gate GO/NO-GO 흐름을 직접 이해하고 설명할 수 있도록 구성하는 것입니다.

---

### 15-1. 학습 및 구현 흐름

| Step | File | Purpose |
|---|---|---|
| 01 | `app/python_basic_study/01_python_basic.py` | 변수, 조건문, expected/actual 비교, assert 기반 PASS/FAIL 확인 |
| 02 | `app/python_basic_study/02_function_basic.py` | 상태값/배터리 검증 로직을 함수로 분리 |
| 03 | `app/python_basic_study/03_list_dict_basic.py` | 리스트, 딕셔너리, for문을 활용한 테스트 데이터 관리 |
| 04 | `app/python_basic_study/04_test_case_loop_basic.py` | 여러 테스트 케이스 반복 실행 및 AssertionError 확인 |
| 05 | `app/python_basic_study/05_test_result_summary_basic.py` | try-except를 활용한 PASS/FAIL 결과 집계 |
| 06 | `app/python_basic_study/06_quality_gate_basic.py` | FAIL 개수 기준 Quality Gate GO/NO-GO 판정 및 결과 파일 저장 |

---

### 15-2. expected / actual / assert 기반 검증 구조

QA 테스트의 기본 구조는 기대값과 실제값을 비교하는 것입니다.

```python
expected_status = "ready"
actual_status = device_status

assert actual_status == expected_status
```

위 코드는 다음 의미를 가집니다.

- `expected_status`: 테스트에서 기대하는 결과
- `actual_status`: 실제 실행 결과 또는 장비에서 읽어온 값
- `assert`: 기대값과 실제값을 비교하여 PASS/FAIL을 판정하는 구문

QA 관점에서는 다음 흐름과 같습니다.

```text
Expected Result 정의
        ↓
Actual Result 확인
        ↓
Expected와 Actual 비교
        ↓
PASS / FAIL 판정
```

---

### 15-3. 함수 기반 검증 로직 분리

초기에는 상태값과 배터리 값을 직접 비교했지만, 이후 동일한 검증 로직을 재사용할 수 있도록 함수로 분리했습니다.

```python
def check_device_status(actual_status, expected_status):
    assert actual_status == expected_status


def check_battery_level(actual_battery, expected_min_battery):
    assert actual_battery >= expected_min_battery
```

함수로 분리한 이유는 다음과 같습니다.

- 같은 검증 로직을 반복해서 사용할 수 있음
- 테스트 코드의 가독성이 좋아짐
- 상태값 검증과 배터리 기준 검증의 역할이 명확해짐
- 나중에 pytest 테스트 함수 구조로 확장하기 쉬움

---

### 15-4. 리스트 / 딕셔너리 기반 테스트 케이스 관리

여러 테스트 케이스를 관리하기 위해 리스트와 딕셔너리 구조를 사용했습니다.

```python
test_cases = [
    {
        "test_id": "TC_001",
        "device_status": "ready",
        "expected_status": "ready",
        "battery_level": 85,
        "expected_min_battery": 50
    }
]
```

각 항목의 의미는 다음과 같습니다.

| Key | Meaning |
|---|---|
| `test_id` | 테스트 케이스 ID |
| `device_status` | 실제 장비 상태값 |
| `expected_status` | 기대 상태값 |
| `battery_level` | 실제 배터리 수치 |
| `expected_min_battery` | 최소 배터리 기준값 |

QA 관점에서 이 구조는 테스트 케이스 표를 코드로 표현한 것입니다.

---

### 15-5. for문 기반 다중 테스트 케이스 실행

리스트에 저장된 여러 테스트 케이스를 하나씩 실행하기 위해 `for`문을 사용했습니다.

```python
for test_case in test_cases:
    actual_status = test_case["device_status"]
    expected_status = test_case["expected_status"]

    assert actual_status == expected_status
```

`for test_case in test_cases:`의 의미는 다음과 같습니다.

```text
test_cases 목록 안에 있는 테스트 케이스를 하나씩 꺼내서
매번 test_case라는 이름으로 사용한다.
```

이를 통해 테스트 케이스가 1개가 아니라 여러 개로 늘어나도 동일한 검증 흐름으로 반복 실행할 수 있습니다.

---

### 15-6. try-except 기반 PASS/FAIL 결과 집계

일반 Python 실행에서는 `assert`가 실패하면 프로그램이 즉시 중단됩니다.  
하지만 QA 자동화에서는 특정 테스트가 실패하더라도 전체 테스트 결과를 끝까지 확인해야 합니다.

이를 위해 `try-except` 구조를 사용했습니다.

```python
try:
    assert actual_status == expected_status
    assert actual_battery >= expected_min_battery

    pass_count = pass_count + 1

except AssertionError:
    fail_count = fail_count + 1
```

이 구조를 통해 다음 흐름을 구성했습니다.

```text
TC_001 PASS
TC_002 PASS
TC_003 FAIL
        ↓
전체 테스트 수 / PASS 수 / FAIL 수 집계
```

QA 관점에서는 테스트 실패를 단순 오류로 끝내지 않고, 결과 Summary로 기록하기 위한 구조입니다.

---

### 15-7. Quality Gate GO / NO-GO 판정

PASS/FAIL 집계 결과를 기반으로 Quality Gate를 판정했습니다.

```python
if fail_count == 0:
    quality_gate_result = "GO"
else:
    quality_gate_result = "NO-GO"
```

판정 기준은 다음과 같습니다.

```text
FAIL Count = 0  → Quality Gate: GO
FAIL Count > 0  → Quality Gate: NO-GO
```

즉, 테스트가 모두 통과하면 다음 단계 진행이 가능하다고 판단하고, 하나라도 실패하면 릴리즈 또는 다음 단계 진행을 보류하는 구조입니다.

---

### 15-8. Quality Gate 결과 파일 저장

Quality Gate 결과는 터미널 출력으로만 끝내지 않고, 파일로 저장했습니다.

```python
with open("reports/quality_gate_basic.txt", "w", encoding="utf-8") as file:
    file.write("Quality Gate Result\n")
    file.write("-------------------\n")
    file.write("Total Test Cases: " + str(len(test_cases)) + "\n")
    file.write("PASS Count: " + str(pass_count) + "\n")
    file.write("FAIL Count: " + str(fail_count) + "\n")
    file.write("Quality Gate: " + quality_gate_result + "\n")
```

생성 파일:

```text
reports/quality_gate_basic.txt
```

NO-GO 예시:

```text
Quality Gate Result
-------------------
Total Test Cases: 3
PASS Count: 2
FAIL Count: 1
Quality Gate: NO-GO
```

GO 예시:

```text
Quality Gate Result
-------------------
Total Test Cases: 3
PASS Count: 3
FAIL Count: 0
Quality Gate: GO
```

---

### 15-9. QA 관점에서의 의미

이 확장 작업은 Python 문법 학습 자체가 목적이 아니라, QA 자동화에서 필요한 검증 흐름을 직접 이해하고 구성하기 위한 단계입니다.

구현한 핵심은 다음과 같습니다.

- 테스트 데이터 관리
- 기대값 / 실제값 비교
- assert 기반 PASS/FAIL 판정
- 함수 기반 검증 로직 분리
- 리스트 / 딕셔너리 기반 테스트 케이스 관리
- for문 기반 다중 테스트 케이스 실행
- try-except 기반 결과 집계
- Quality Gate GO/NO-GO 판정
- 결과 파일 Artifact 저장

이를 통해 기존 Manual QA 경험을 Python 기반 자동화 검증 로직으로 확장했습니다.

---

## 16. Git / GitHub 연동

본 프로젝트는 Git으로 로컬 변경 이력을 관리하고, GitHub Repository와 연동했습니다.

초기 Git 저장소 생성:

```bat
git init
```

파일 추가:

```bat
git add .
```

Commit 생성:

```bat
git commit -m "Initial QA CI automation project"
```

GitHub 원격 저장소 연결:

```bat
git remote add origin https://github.com/Suhwan-Quality/robot-qa-cicd-pipeline.git
```

GitHub 업로드:

```bat
git push -u origin main
```

이후 변경사항 반영 시 다음 명령어를 사용합니다.

```bat
git status
git add -A
git commit -m "Commit message"
git push
```

---

## 17. GitHub Actions CI Workflow

본 프로젝트는 GitHub Actions를 활용하여 `main` branch에 push가 발생하거나 Pull Request가 생성될 때 자동으로 QA 테스트가 실행되도록 구성했습니다.

GitHub Actions CI Workflow는 `.github/workflows/ci.yml` 파일에 정의되어 있으며, 로컬에서 구성한 `Smoke Test → Regression Test → Quality Gate` 흐름과 동일한 구조로 동작하도록 개선했습니다.

---

### CI Workflow Execution Flow

```text
1. Source Code Checkout
2. Python 3.12 환경 구성
3. requirements.txt 기반 패키지 설치
4. reports / logs 폴더 생성
5. 환경 정보 저장
6. Smoke Test 실행
7. Regression Test 실행
8. Quality Gate 결과 저장
9. HTML / XML Report 생성
10. 테스트 실행 로그 저장
11. Artifact 업로드
```

---

### Workflow Trigger

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:
```

* `push`: main branch에 코드가 push되면 자동 실행
* `pull_request`: main branch 대상 Pull Request 생성 시 자동 실행
* `workflow_dispatch`: GitHub Actions 화면에서 수동 실행 가능

---

### GitHub Actions 실행 결과

GitHub Actions 실행 결과 `qa-test` Job이 정상 완료되었습니다.

```text
Workflow: QA CI Pipeline
Job: qa-test
Status: Success
Total Duration: 47s
Artifact Name: qa-test-artifacts
```

GitHub Actions 실행 상세 화면에서 다음 단계가 모두 정상 완료되었습니다.

```text
Set up job
Checkout source code
Set up Python
Install required packages
Create report and log folders
Save environment information
Run Smoke Tests
Run Regression Tests
Save Quality Gate Result
Upload test artifacts
Complete job
```

---

### Uploaded Artifacts

GitHub Actions 실행 후 다음 산출물이 `qa-test-artifacts`로 저장됩니다.

| Artifact                         | Description                             |
| -------------------------------- | --------------------------------------- |
| `reports/smoke_result.xml`       | Smoke Test 결과를 담은 JUnit XML Report      |
| `reports/smoke_result.html`      | 사람이 확인 가능한 Smoke Test HTML Report       |
| `reports/regression_result.xml`  | Regression Test 결과를 담은 JUnit XML Report |
| `reports/regression_result.html` | 사람이 확인 가능한 Regression Test HTML Report  |
| `reports/quality_gate.txt`       | 테스트 결과 기반 GO / NO-GO 판정 결과              |
| `logs/smoke_test_log.txt`        | Smoke Test 실행 로그                        |
| `logs/regression_test_log.txt`   | Regression Test 실행 로그                   |
| `logs/environment_info.txt`      | Python 및 패키지 버전 정보                      |

---

## 18. Troubleshooting: GitHub Actions Shell Syntax Error

GitHub Actions 최초 실행 시 `Create report and log folders` 단계에서 실패가 발생했습니다.

### Failure Point

```text
Step: Create report and log folders
Command: if not exist reports mkdir reports
Result: Failed
```

### Error Message

```text
ParserError
Missing '(' after 'if' in if statement.
Process completed with exit code 1.
```

### Root Cause

로컬 Windows batch 환경에서는 아래 CMD 문법이 정상 동작합니다.

```bat
if not exist reports mkdir reports
if not exist logs mkdir logs
```

하지만 GitHub Actions의 Windows Runner에서는 기본적으로 PowerShell 기반으로 `run` 명령을 해석했습니다.

따라서 CMD 문법인 `if not exist`를 PowerShell이 해석하지 못해 Syntax Error가 발생했습니다.

---

### Corrective Action

GitHub Actions workflow의 폴더 생성 명령을 PowerShell 호환 문법으로 수정했습니다.

```powershell
New-Item -ItemType Directory -Force -Path reports | Out-Null
New-Item -ItemType Directory -Force -Path logs | Out-Null
```

환경 정보 저장 및 Quality Gate 결과 저장도 PowerShell 방식으로 수정했습니다.

```powershell
python --version | Out-File -FilePath logs/environment_info.txt -Encoding utf8
python -m pip freeze | Out-File -FilePath logs/environment_info.txt -Append -Encoding utf8
```

Smoke Test와 Regression Test 실행 후 결과에 따라 Quality Gate 파일이 생성되도록 구성했습니다.

```powershell
if ($LASTEXITCODE -ne 0) {
  "NO-GO" | Out-File -FilePath reports/quality_gate.txt -Encoding utf8
  exit $LASTEXITCODE
}
```

모든 테스트가 정상 통과한 경우 다음과 같이 GO 결과를 저장합니다.

```powershell
"GO" | Out-File -FilePath reports/quality_gate.txt -Encoding utf8
```

---

### Result After Fix

Workflow 수정 후 GitHub Actions CI Pipeline이 정상 실행되었습니다.

```text
Workflow: QA CI Pipeline
Job: qa-test
Status: Success
Artifacts: qa-test-artifacts generated
```

최종적으로 GitHub Actions에서 다음 단계가 모두 성공했습니다.

```text
Run Smoke Tests
Run Regression Tests
Save Quality Gate Result
Upload test artifacts
```

---

### QA 관점에서의 의미

이번 오류는 단순한 설정 오류가 아니라, 로컬 실행 환경과 CI 실행 환경의 차이로 인해 발생한 문제입니다.

이를 통해 다음 사항을 확인했습니다.

* 로컬 Windows batch 명령어와 GitHub Actions PowerShell 명령어의 차이
* CI 실패 로그 분석 방법
* 실패 단계 식별
* 원인 분석 후 workflow 수정
* 재실행을 통한 CI 정상화 확인
* Smoke / Regression 분리 구조로 CI Pipeline 개선

본 Troubleshooting 과정은 실제 QA/검증 업무에서 중요한 실패 로그 분석, 원인 파악, 수정 검증 흐름과 연결됩니다.

---

## 19. 실제 서버 / 장비 연동 시 확장 구조

현재 프로젝트는 Mock Device 기반으로 구성되어 있지만, 실제 실무에서는 서버 또는 장비와 연동하여 동일한 구조로 확장할 수 있습니다.

예상 확장 구조는 다음과 같습니다.

```text
GitHub Push 또는 Jenkins Build Trigger
        ↓
빌드 산출물 생성
        ↓
Test Server 또는 Robot Controller에 배포
        ↓
Smoke Test 실행
        ↓
API / 장비 상태 / Version / Health Check 검증
        ↓
Regression Test 실행
        ↓
주요 기능 및 예외처리 검증
        ↓
Log / Report / Artifact 저장
        ↓
Quality Gate GO / NO-GO 판단
        ↓
Jira 또는 Issue Tracker에 실패 결과 등록
```

---

### 실제 서버 연동 예시

실제 서버와 연동할 경우 Mock Device 대신 API Client를 사용할 수 있습니다.

예시 구조:

```text
app/
 ├─ api_client.py
 └─ device.py

tests/
 ├─ smoke/
 │   └─ test_server_smoke.py
 └─ regression/
     └─ test_server_regression.py
```

검증 항목 예시:

| Test Type       | Example                           |
| --------------- | --------------------------------- |
| Smoke Test      | 서버 Health Check                   |
| Smoke Test      | Version API 응답 확인                 |
| Smoke Test      | 로그인 또는 인증 기본 동작 확인                |
| Regression Test | 비정상 요청 Error Response 확인          |
| Regression Test | 기존 API 응답 구조 유지 확인                |
| Regression Test | Timeout / Invalid Parameter 처리 확인 |

---

### 실제 장비 연동 예시

로봇 또는 임베디드 장비와 연동할 경우 다음 항목을 테스트할 수 있습니다.

| Test Type       | Example                   |
| --------------- | ------------------------- |
| Smoke Test      | 장비 연결 확인                  |
| Smoke Test      | Firmware / SW Version 조회  |
| Smoke Test      | Motor / Sensor 기본 상태 확인   |
| Smoke Test      | E-Stop 상태 확인              |
| Regression Test | 비정상 명령 입력 시 Error Code 확인 |
| Regression Test | 통신 끊김 상태에서의 예외처리 확인       |
| Regression Test | 장비 상태 전환 후 기존 기능 유지 확인    |

실제 장비 연동 시에는 USB, Serial, CAN, Ethernet, REST API, Socket 통신 등 프로젝트 환경에 맞는 통신 방식을 사용할 수 있습니다.

---

## 20. QA 관점에서의 최종 의미

본 프로젝트는 단순히 Python 테스트 코드를 실행한 것이 아니라, QA 검증 관점에서 다음 흐름을 직접 구성한 개인 포트폴리오 프로젝트입니다.

```text
테스트 대상 정의
        ↓
Smoke / Regression Test Suite 분리
        ↓
로컬 테스트 실행
        ↓
Local CI Pipeline 구성
        ↓
GitHub Repository 연동
        ↓
GitHub Actions CI 자동 실행
        ↓
HTML / XML Report 생성
        ↓
Log / Environment Info Artifact 저장
        ↓
Quality Gate GO / NO-GO 판단
```

이를 통해 수동 검증 중심의 QA 경험을 CI 기반 자동화 검증 흐름으로 확장하는 기본 구조를 학습하고 구현했습니다.

실제 업무에서는 이 구조를 다음과 같이 확장할 수 있습니다.

* 실제 장비 또는 서버 API와 연동한 Smoke Test 수행
* 빌드 산출물 배포 후 자동 테스트 실행
* 테스트 결과 기반 Release GO / NO-GO 판단
* 실패 로그 기반 원인 분석 및 이슈 등록
* Jenkins, GitLab CI, GitHub Actions 등 CI 도구와 연동
* Test Report 및 Artifact를 품질 증적으로 보관

본 프로젝트는 QA Engineer 관점에서 CI/CD 환경의 테스트 실행 구조, 리포트 생성, 로그 관리, Artifact 저장, Quality Gate 운영 개념을 이해하고 실습하기 위해 구성했습니다.


