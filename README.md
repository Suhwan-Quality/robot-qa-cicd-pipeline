## 14. GitHub Actions CI Workflow

본 프로젝트는 GitHub Actions를 활용하여 main branch에 push가 발생하거나 Pull Request가 생성될 때 자동으로 QA 테스트가 실행되도록 구성했습니다.

GitHub Actions CI Workflow는 `.github/workflows/ci.yml` 파일에 정의되어 있으며, 다음 절차를 자동으로 수행합니다.

```text
1. Source Code Checkout
2. Python 3.12 환경 구성
3. requirements.txt 기반 패키지 설치
4. reports / logs 폴더 생성
5. 환경 정보 저장
6. pytest 기반 자동화 테스트 실행
7. JUnit XML Report 생성
8. HTML Test Report 생성
9. 테스트 실행 로그 저장
10. Quality Gate 결과 저장
11. Artifact 업로드
```

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

### CI Execution Result

GitHub Actions 실행 결과 `qa-test` Job이 정상 완료되었습니다.

```text
Workflow: QA CI Pipeline
Job: qa-test
Status: Success
Total Duration: 48s
Artifacts: 1
Artifact Name: qa-test-artifacts
```

CI 실행을 통해 pytest 기반 자동화 테스트가 정상 수행되었으며, 테스트 결과 산출물이 GitHub Actions Artifact로 저장되었습니다.

---

### Uploaded Artifacts

GitHub Actions 실행 후 다음 산출물이 `qa-test-artifacts`로 저장됩니다.

| Artifact               | Description                 |
| ---------------------- | --------------------------- |
| `result.xml`           | JUnit XML 기반 테스트 결과 파일      |
| `result.html`          | 사람이 확인 가능한 HTML Test Report |
| `quality_gate.txt`     | 테스트 결과 기반 GO / NO-GO 판정 결과  |
| `test_log.txt`         | pytest 실행 로그                |
| `environment_info.txt` | Python 및 패키지 버전 정보          |

---

### GitHub Actions CI 관점에서의 의미

본 Workflow를 통해 로컬에서만 실행되던 QA 자동화 테스트를 GitHub Actions CI 환경으로 확장했습니다.

```text
Local Test Execution
        ↓
GitHub Repository Push
        ↓
GitHub Actions Trigger
        ↓
Automated QA Test Execution
        ↓
Report / Log Artifact Upload
        ↓
CI Result Review
```

이를 통해 코드 변경 시 자동으로 테스트가 수행되고, 테스트 결과와 로그가 Artifact로 보관되는 CI 기반 QA 검증 흐름을 구성했습니다.

---

## 15. Troubleshooting: GitHub Actions Shell Syntax Error

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

### Result After Fix

Workflow 수정 후 GitHub Actions CI Pipeline이 정상 실행되었습니다.

```text
Workflow: QA CI Pipeline
Job: qa-test
Status: Success
Artifacts: qa-test-artifacts generated
```

### QA 관점에서의 의미

이번 오류는 단순한 설정 오류가 아니라, 로컬 실행 환경과 CI 실행 환경의 차이로 인해 발생한 문제입니다.

이를 통해 다음 사항을 확인했습니다.

* 로컬 Windows batch 명령어와 GitHub Actions PowerShell 명령어의 차이
* CI 실패 로그 분석 방법
* 실패 단계 식별
* 원인 분석 후 workflow 수정
* 재실행을 통한 CI 정상화 확인

본 Troubleshooting 과정은 실제 QA/검증 업무에서 중요한 실패 로그 분석, 원인 파악, 수정 검증 흐름과 연결됩니다.
