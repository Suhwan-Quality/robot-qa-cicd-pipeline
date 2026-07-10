# ============================================================
# tests/smoke/test_api_smoke.py
# ============================================================
#
# 이 파일은 FastAPI 기반 Mock Robot API의 Smoke Test를 정의하는 파일이다.
#
# Smoke Test란?
# - 시스템이 기본적으로 테스트 가능한 상태인지 빠르게 확인하는 테스트이다.
# - 여기서는 API 서버가 기본 응답을 정상적으로 반환하는지 확인한다.
#
# 이 파일에서 검증하는 API:
# - GET /health
# - GET /version
# - GET /motor/status
#
# QA 관점 의미:
# - 서버 상태 확인
# - 버전 정보 확인
# - 장비 모터 상태 확인
#
# 기존 테스트와의 차이:
# - 기존에는 MockRobotDevice 함수를 직접 호출해서 검증했다.
# - 이번에는 FastAPI API를 호출하고, HTTP Status Code와 JSON Response Body를 검증한다.
# ============================================================


# FastAPI의 TestClient를 가져온다.
#
# TestClient는 어디에 있는가?
# - fastapi.testclient 모듈 안에 있다.
#
# 왜 사용하는가?
# - 실제 서버를 따로 실행하지 않아도 테스트 코드 안에서 API를 호출할 수 있게 해준다.
#
# 일반적으로 API를 테스트할 때는 Postman이나 브라우저, curl 같은 도구를 사용할 수 있다.
# 하지만 자동화 테스트에서는 사람이 직접 호출하면 안 되기 때문에,
# pytest 코드 안에서 API를 호출할 수 있는 TestClient를 사용한다.
#
# 쉽게 말하면:
# - TestClient = 테스트 코드 안에서 사용하는 가짜 API 호출 도구
# - Postman과 비슷한 역할을 pytest 코드 안에서 수행한다고 이해하면 된다.
from fastapi.testclient import TestClient


# app/api_server.py 파일에 정의된 app 객체를 가져온다.
#
# app은 어디에 있는가?
# - app/api_server.py 파일 안에 있다.
#
# app은 무엇인가?
# - FastAPI()로 생성한 API 애플리케이션 객체이다.
# - /health, /version, /motor/status API가 이 app 객체에 등록되어 있다.
#
# 왜 가져오는가?
# - TestClient가 어떤 API 서버를 테스트해야 하는지 알아야 하기 때문이다.
#
# 즉, 아래 import는:
# "app/api_server.py에 만든 Mock Robot API Server를 이 테스트 파일에서 사용하겠다"
# 라는 의미이다.
from app.api_server import app


# TestClient 객체를 생성한다.
#
# client는 무엇인가?
# - API를 호출하기 위한 테스트용 클라이언트 객체이다.
#
# 왜 TestClient(app)처럼 app을 넣는가?
# - app 안에 등록된 API 주소들을 대상으로 테스트하기 위해서이다.
#
# 이 client를 사용하면 아래처럼 API를 호출할 수 있다.
# - client.get("/health")
# - client.get("/version")
# - client.get("/motor/status")
#
# 실제 서버를 실행하지 않아도 되는 이유:
# - TestClient가 FastAPI app을 내부적으로 직접 호출해주기 때문이다.
#
# QA 관점:
# - 사람이 Postman으로 API를 눌러보는 작업을 pytest 코드로 자동화한 구조이다.
client = TestClient(app)


def test_health_api_returns_ok():
    # ------------------------------------------------------------
    # Test Case: GET /health API Smoke Test
    # ------------------------------------------------------------
    #
    # 이 테스트 함수는 /health API가 정상적으로 응답하는지 검증한다.
    #
    # 이 함수는 어디에서 실행되는가?
    # - pytest가 이 파일을 실행할 때 자동으로 수집해서 실행한다.
    #
    # 왜 pytest가 이 함수를 테스트로 인식하는가?
    # - 함수 이름이 test_로 시작하기 때문이다.
    #
    # 이 테스트가 호출하는 API 함수는 어디에 있는가?
    # - app/api_server.py 안의 health_check() 함수이다.
    #
    # 호출 흐름:
    # test_health_api_returns_ok()
    #   → client.get("/health")
    #   → app/api_server.py의 @app.get("/health")
    #   → health_check()
    #   → {"status": "ok"} 반환
    #
    # QA 테스트 케이스로 보면:
    #
    # Test Step:
    # - GET /health API 호출
    #
    # Expected Result:
    # - HTTP Status Code가 200이어야 한다.
    # - Response Body가 {"status": "ok"} 이어야 한다.
    #
    # QA 의미:
    # - API 서버가 기본적으로 살아 있고 정상 응답하는지 확인한다.
    # - 후속 API 테스트를 진행하기 전 가장 먼저 확인할 수 있는 Smoke Test이다.

    # GET 방식으로 /health API를 호출한다.
    #
    # client.get("/health")는 어떤 함수를 호출하는가?
    # - app/api_server.py의 health_check() 함수가 실행된다.
    #
    # 왜 호출하는가?
    # - Mock Robot API Server가 정상 상태인지 확인하기 위해서이다.
    #
    # response 변수에는 API 호출 결과가 저장된다.
    # 이 안에는 status_code와 response body가 들어 있다.
    response = client.get("/health")

    # HTTP Status Code가 200인지 확인한다.
    #
    # response.status_code는 무엇인가?
    # - API 응답의 HTTP 상태 코드이다.
    #
    # 왜 200을 기대하는가?
    # - 200은 요청이 정상 처리되었다는 의미이기 때문이다.
    #
    # 주요 HTTP 상태 코드 예:
    # - 200: 정상
    # - 400: 잘못된 요청
    # - 404: API 주소 없음
    # - 500: 서버 내부 오류
    #
    # assert는 pytest의 PASS/FAIL 판정 구문이다.
    # 실제 status_code가 200이 아니면 이 테스트는 FAIL 처리된다.
    assert response.status_code == 200

    # API 응답 Body가 {"status": "ok"}인지 확인한다.
    #
    # response.json()은 무엇인가?
    # - API 응답 Body를 Python 딕셔너리 형태로 변환하는 함수이다.
    #
    # 왜 json()을 호출하는가?
    # - API 응답은 JSON 형태로 오기 때문에,
    #   Python 코드에서 비교하기 쉬운 딕셔너리로 바꿔야 한다.
    #
    # app/api_server.py의 health_check() 함수는 {"status": "ok"}를 반환한다.
    # 따라서 테스트에서도 동일한 값을 기대한다.
    #
    # key 또는 value가 다르면 테스트는 FAIL 처리된다.
    assert response.json() == {
        "status": "ok"
    }


def test_version_api_returns_version():
    # ------------------------------------------------------------
    # Test Case: GET /version API Smoke Test
    # ------------------------------------------------------------
    #
    # 이 테스트 함수는 /version API가 정상적으로 버전 정보를 반환하는지 검증한다.
    #
    # 이 테스트가 호출하는 API 함수는 어디에 있는가?
    # - app/api_server.py 안의 version_check() 함수이다.
    #
    # 호출 흐름:
    # test_version_api_returns_version()
    #   → client.get("/version")
    #   → app/api_server.py의 @app.get("/version")
    #   → version_check()
    #   → {"version": "1.0.0"} 반환
    #
    # QA 테스트 케이스로 보면:
    #
    # Test Step:
    # - GET /version API 호출
    #
    # Expected Result:
    # - HTTP Status Code가 200이어야 한다.
    # - Response Body가 {"version": "1.0.0"} 이어야 한다.
    #
    # QA 의미:
    # - 테스트 대상 서버 또는 장비 제어 SW의 버전을 확인한다.
    # - 실제 업무에서는 배포된 빌드 버전이 맞는지 확인하는 기본 검증 항목이다.

    # GET 방식으로 /version API를 호출한다.
    #
    # client.get("/version")는 어떤 함수를 호출하는가?
    # - app/api_server.py의 version_check() 함수가 실행된다.
    #
    # 왜 호출하는가?
    # - API가 기대한 버전 정보를 반환하는지 확인하기 위해서이다.
    #
    # 호출 결과는 response 변수에 저장된다.
    response = client.get("/version")

    # HTTP Status Code가 200인지 확인한다.
    #
    # 200이 아니면 /version API가 정상 처리되지 않았다는 뜻이다.
    # 예를 들어 API 주소가 잘못되면 404,
    # 내부 코드 오류가 있으면 500이 나올 수 있다.
    assert response.status_code == 200

    # Response Body가 기대값과 같은지 확인한다.
    #
    # app/api_server.py의 version_check() 함수는 {"version": "1.0.0"}을 반환한다.
    #
    # 왜 이 값을 검증하는가?
    # - API가 단순히 200으로 응답하는지만 보는 것이 아니라,
    #   실제 Body 값도 기대한 버전인지 확인해야 하기 때문이다.
    #
    # QA 관점에서는 status code와 body를 함께 검증해야 API 응답 품질을 더 정확히 볼 수 있다.
    assert response.json() == {
        "version": "1.0.0"
    }


def test_motor_status_api_returns_ready():
    # ------------------------------------------------------------
    # Test Case: GET /motor/status API Smoke Test
    # ------------------------------------------------------------
    #
    # 이 테스트 함수는 /motor/status API가 정상적으로 모터 상태를 반환하는지 검증한다.
    #
    # 이 테스트가 호출하는 API 함수는 어디에 있는가?
    # - app/api_server.py 안의 motor_status_check() 함수이다.
    #
    # 호출 흐름:
    # test_motor_status_api_returns_ready()
    #   → client.get("/motor/status")
    #   → app/api_server.py의 @app.get("/motor/status")
    #   → motor_status_check()
    #   → MockRobotDevice() 생성
    #   → device.connect() 호출
    #   → device.read_motor_status() 호출
    #   → {"motor_status": "READY"} 반환
    #
    # QA 테스트 케이스로 보면:
    #
    # Test Step:
    # - GET /motor/status API 호출
    #
    # Expected Result:
    # - HTTP Status Code가 200이어야 한다.
    # - Response Body가 {"motor_status": "READY"} 이어야 한다.
    #
    # QA 의미:
    # - API를 통해 장비의 기본 모터 상태를 확인한다.
    # - 내부 MockRobotDevice가 연결 후 READY 상태를 반환하는지 API 응답 기준으로 검증한다.
    # - 실제 장비/서버 검증에서는 장비 기본 준비 상태 확인용 Smoke Test로 연결할 수 있다.

    # GET 방식으로 /motor/status API를 호출한다.
    #
    # client.get("/motor/status")는 어떤 함수를 호출하는가?
    # - app/api_server.py의 motor_status_check() 함수가 실행된다.
    #
    # 왜 호출하는가?
    # - Mock Robot API가 모터 상태를 정상적으로 반환하는지 확인하기 위해서이다.
    #
    # response 변수에는 API 호출 결과가 저장된다.
    response = client.get("/motor/status")

    # HTTP Status Code가 200인지 확인한다.
    #
    # 200은 API 요청이 정상 처리되었다는 의미이다.
    #
    # 만약 app/api_server.py에서 /motor/status 주소가 등록되지 않았다면 404가 나올 수 있다.
    # 만약 motor_status_check() 내부에서 코드 오류가 발생하면 500이 나올 수 있다.
    #
    # 따라서 status_code 검증은 API 호출 자체가 정상 처리되었는지 확인하는 1차 검증이다.
    assert response.status_code == 200

    # Response Body가 {"motor_status": "READY"}인지 확인한다.
    #
    # response.json()은 API 응답 Body를 Python 딕셔너리로 변환한다.
    #
    # app/api_server.py의 motor_status_check() 함수는 내부적으로:
    # - MockRobotDevice 객체 생성
    # - device.connect() 호출
    # - device.read_motor_status() 호출
    # 을 수행한다.
    #
    # 연결된 MockRobotDevice의 read_motor_status() 기대 결과는 "READY"이다.
    # 따라서 API 응답 Body의 motor_status 값도 "READY"여야 한다.
    #
    # 이 값이 다르면 API 또는 내부 장비 상태 처리 로직에 문제가 있다고 볼 수 있다.
    assert response.json() == {
        "motor_status": "READY"
    }