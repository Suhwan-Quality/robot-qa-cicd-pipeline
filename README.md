\# CI/CD 기반 QA 자동화 검증 환경 구축 실습



\## Mock Robot Device Smoke Test Automation Project



\## 1. 프로젝트 개요



본 프로젝트는 로봇/임베디드 시스템 검증 업무에서 활용 가능한 CI/CD 기반 QA 자동화 검증 환경을 학습하고 구현하기 위한 개인 포트폴리오 프로젝트입니다.



실제 장비가 없는 환경을 가정하여 Mock Robot Device를 구성하고, Python pytest 기반으로 장비 연결, 버전 조회, 모터 상태, 비상정지 상태, 예외 명령 응답에 대한 Smoke Test 및 Negative Test를 자동화했습니다.



본 프로젝트의 목적은 단순 테스트 코드 작성이 아니라, QA 관점에서 테스트 실행, 결과 리포트 생성, 로그 저장, Quality Gate 판단까지 이어지는 기본적인 자동 검증 흐름을 구현하는 것입니다.



\---



\## 2. 프로젝트 목적



\* 수동 검증 항목을 자동화 테스트 케이스로 전환

\* Python/pytest 기반 Smoke Test 구조 이해

\* Mock Device를 활용한 로봇/장비 검증 시나리오 구성

\* JUnit XML Report 및 HTML Test Report 생성

\* 테스트 실행 로그 및 환경 정보 저장

\* run\_ci.bat 기반 Local CI Pipeline 구성

\* 테스트 결과 기반 Quality Gate GO/NO-GO 판단 흐름 구현



\---



\## 3. 사용 기술



\* Python 3.14.3

\* pytest 9.1.0

\* pytest-html 4.2.0

\* Windows PowerShell

\* Python venv 가상환경

\* Git

\* Batch Script

\* JUnit XML Report

\* HTML Test Report



\---



\## 4. 프로젝트 구조



```text

qa-cicd-practice/

&#x20;├─ app/

&#x20;│   ├─ \_\_init\_\_.py

&#x20;│   └─ device.py

&#x20;├─ tests/

&#x20;│   ├─ \_\_init\_\_.py

&#x20;│   └─ test\_device.py

&#x20;├─ reports/

&#x20;│   ├─ result.xml

&#x20;│   ├─ result.html

&#x20;│   └─ quality\_gate.txt

&#x20;├─ logs/

&#x20;│   ├─ test\_log.txt

&#x20;│   └─ environment\_info.txt

&#x20;├─ requirements.txt

&#x20;├─ run\_ci.bat

&#x20;├─ .gitignore

&#x20;└─ README.md

```



\---



\## 5. 테스트 대상



테스트 대상은 실제 로봇 장비가 아닌 Mock Robot Device입니다.



Mock Device는 다음 기능을 제공합니다.



\* 장비 연결

\* SW 버전 조회

\* 모터 상태 조회

\* 비상정지 상태 조회

\* 명령어 응답 처리

\* 비정상 명령 예외 응답 처리



\---



\## 6. 자동화 테스트 항목



| TC ID        | 테스트 항목                          | 검증 목적                     |

| ------------ | ------------------------------- | ------------------------- |

| TC\_SMOKE\_001 | Device Connection Test          | 장비 연결 상태 확인               |

| TC\_SMOKE\_002 | Version Read Test               | 연결 후 SW 버전 조회 확인          |

| TC\_SMOKE\_003 | Motor Status Test               | 모터 상태 READY 여부 확인         |

| TC\_SMOKE\_004 | Emergency Stop Status Test      | 비상정지 기본 상태 확인             |

| TC\_NEG\_001   | Invalid Command Test            | 비정상 명령 입력 시 Error Code 확인 |

| TC\_NEG\_002   | Read Version Without Connection | 미연결 상태에서 버전 조회 시 예외 응답 확인 |



\---



\## 7. 설치 및 실행 방법



\### 7-1. 가상환경 생성



```bat

python -m venv .venv

```



\### 7-2. 가상환경 활성화



```bat

.\\.venv\\Scripts\\activate

```



\### 7-3. 필요 패키지 설치



```bat

python -m pip install -r requirements.txt

```



\### 7-4. 테스트 단독 실행



```bat

python -m pytest tests

```



\### 7-5. 테스트 상세 결과 확인



```bat

python -m pytest tests -v

```



\### 7-6. JUnit XML 및 HTML Report 생성



```bat

python -m pytest tests --junitxml=reports\\result.xml --html=reports\\result.html --self-contained-html

```



\### 7-7. Local CI Pipeline 실행



```bat

.\\run\_ci.bat

```



\---



\## 8. 테스트 실행 결과



pytest 실행 결과 총 6개의 테스트 케이스가 정상적으로 수집 및 수행되었습니다.



```text

collected 6 items

tests\\test\_device.py ...... \[100%]

6 passed

```



HTML Report에서는 6개 테스트가 모두 Passed로 표시되며, JUnit XML Report에는 tests="6", failures="0", errors="0" 결과가 기록됩니다.



\---



\## 9. 산출물



| 산출물                       | 설명                                                       |

| ------------------------- | -------------------------------------------------------- |

| reports/result.html       | 사람이 확인 가능한 HTML Test Report            |

| reports/result.xml        | Jenkins/GitHub Actions 등 CI 도구가 읽을 수 있는 JUnit XML Report |

| logs/test\_log.txt         | 테스트 실행 로그                                                |

| logs/environment\_info.txt | Python 및 패키지 버전 정보                                       |

| reports/quality\_gate.txt  | Quality Gate GO/NO-GO 결과                                 |



\---



\## 10. Local CI Pipeline 구성



본 프로젝트에서는 run\_ci.bat 파일을 통해 로컬 CI Pipeline을 구성했습니다.



run\_ci.bat 실행 시 다음 절차가 자동으로 수행됩니다.



```text

1\. 필요 패키지 설치 확인

2\. 테스트 환경 정보 저장

3\. pytest 기반 자동화 테스트 실행

4\. JUnit XML Report 생성

5\. HTML Test Report 생성

6\. 테스트 로그 저장

7\. 테스트 결과 기반 Quality Gate 판정

```



테스트가 모두 통과하면 다음 결과가 출력됩니다.



```text

\[RESULT] TEST PASSED

\[QUALITY GATE] GO

```



테스트가 실패하면 Quality Gate는 NO-GO로 판정됩니다.



\---



\## 11. QA 관점에서의 의미



본 프로젝트는 단순한 Python 테스트 코드 작성이 아니라, 실제 QA 검증 업무에서 필요한 다음 흐름을 학습하고 구현하기 위한 목적을 가집니다.



```text

테스트 대상 정의

&#x20;       ↓

테스트 케이스 설계

&#x20;       ↓

자동화 테스트 실행

&#x20;       ↓

Pass/Fail 판정

&#x20;       ↓

리포트 및 로그 저장

&#x20;       ↓

Quality Gate 판단

```



특히 로봇/임베디드 시스템 검증에서는 장비 연결 상태, 버전 정보, 상태값, 예외 응답, 로그 분석이 중요하므로 이를 Mock Device 기반으로 단순화하여 구현했습니다.



\---



\## 12. 향후 확장 계획



본 프로젝트는 다음 단계로 확장 예정입니다.



\* Smoke Test / Regression Test 폴더 분리

\* 실패 케이스 및 Fail Log 분석 예시 추가

\* GitHub Actions 기반 CI Workflow 구성

\* Jenkins Pipeline 연동

\* Artifact 업로드 및 보관 구조 구현

\* Pull Request 기준 자동 테스트 실행

\* 빌드별 테스트 결과 추적 구조 확장



\---



\## 13. 포트폴리오 활용 목적



본 프로젝트는 실제 회사 업무로 수행한 것이 아니라, CI/CD 기반 QA 자동화 검증 흐름을 이해하고 개인적으로 학습 및 구현한 포트폴리오 프로젝트입니다.



이를 통해 수동 검증 중심의 QA 경험을 테스트 자동화, 리포트 관리, 로그 기반 분석, Quality Gate 운영 개념으로 확장하고자 했습니다.



