# ============================================================
# tests/regression/test_api_regression.py
# ============================================================
#
# 이 파일은 FastAPI 기반 Mock Robot API의 Regression Test를 정의하는 파일이다.
#
# Regression Test란?
# - 기존 기능이나 예외처리 로직이 코드 수정 후에도 깨지지 않았는지 확인하는 테스트이다.
#
# 이 파일에서 검증하는 API:
# - GET /motor/status/not-connected
#
# QA 관점 의미:
# - 장비가 연결되지 않은 상태에서 motor status를 요청했을 때
#   기대한 Error Response가 반환되는지 검증한다.
#
# Smoke Test와의 차이:
# - Smoke Test는 정상 동작 중심이다.
# - Regression Test는 기존 예외처리, 방어 로직, Negative Case가 유지되는지 확인한다.
# ============================================================


# FastAPI의 TestClient를 가져온다.
#
# TestClient는 어디에 있는가?
# - fastapi.testclient 모듈 안에 있다.
#
# 왜 사용하는가?
# - 실제 API 서버를 따로 실행하지 않아도
#   pytest 코드 안에서 API를 호출할 수 있기 때문이다.
#
# 쉽게 말하면:
# - 사람이 Postman으로 API를 호출하는 대신,
#   pytest 코드가 TestClient로 API를 자동 호출한다.
from fastapi.testclient import TestClient


# app/api_server.py 파일에 정의된 app 객체를 가져온다.
#
# app은 어디에 있는가?
# - app/api_server.py 파일 안에 있다.
#
# app은 무엇인가?
# - FastAPI()로 생성한 API 애플리케이션 객체이다.
# - /health, /version, /motor/status, /motor/status/not-connected API가 등록되어 있다.
#
# 왜 가져오는가?
# - TestClient가 어떤 API 서버를 대상으로 테스트해야 하는지 알아야 하기 때문이다.
from app.api_server import app


# TestClient 객체를 생성한다.
#
# client는 무엇인가?
# - API를 호출하기 위한 테스트용 클라이언트 객체이다.
#
# 왜 TestClient(app)을 사용하는가?
# - app에 등록된 API들을 테스트 코드에서 호출하기 위해서이다.
#
# 이 client를 사용하면 아래처럼 API를 호출할 수 있다.
# - client.get("/motor/status/not-connected")
client = TestClient(app)


def test_motor_status_api_without_connection_returns_error():
    # ------------------------------------------------------------
    # Test Case: GET /motor/status/not-connected API Regression Test
    # ------------------------------------------------------------
    #
    # 이 테스트 함수는 미연결 상태의 motor status API가
    # 기대한 예외 응답을 반환하는지 검증한다.
    #
    # 이 테스트가 호출하는 API 함수는 어디에 있는가?
    # - app/api_server.py 안의 motor_status_without_connection_check() 함수이다.
    #
    # 호출 흐름:
    # test_motor_status_api_without_connection_returns_error()
    #   → client.get("/motor/status/not-connected")
    #   → app/api_server.py의 @app.get("/motor/status/not-connected")
    #   → motor_status_without_connection_check()
    #   → MockRobotDevice() 생성
    #   → device.connect()는 호출하지 않음
    #   → device.read_motor_status() 호출
    #   → {"motor_status": "ERROR_NOT_CONNECTED"} 반환
    #
    # QA 테스트 케이스로 보면:
    #
    # Test Step:
    # - GET /motor/status/not-connected API 호출
    #
    # Expected Result:
    # - HTTP Status Code가 200이어야 한다.
    # - Response Body가 {"motor_status": "ERROR_NOT_CONNECTED"} 이어야 한다.
    #
    # QA 의미:
    # - 장비 연결 없이 motor status를 요청했을 때 정상 READY가 나오면 안 된다.
    # - 미연결 상태에서는 ERROR_NOT_CONNECTED가 반환되어야 한다.
    # - 이 예외처리 로직이 이후 코드 수정에도 유지되는지 Regression Test로 확인한다.

    # GET 방식으로 /motor/status/not-connected API를 호출한다.
    #
    # client.get("/motor/status/not-connected")는 어떤 함수를 호출하는가?
    # - app/api_server.py의 motor_status_without_connection_check() 함수가 실행된다.
    #
    # 왜 호출하는가?
    # - 미연결 상태에서 motor status API가 기대한 Error Response를 반환하는지 확인하기 위해서이다.
    #
    # 호출 결과는 response 변수에 저장된다.
    response = client.get("/motor/status/not-connected")

    # HTTP Status Code가 200인지 확인한다.
    #
    # 왜 에러 상황인데 200을 기대하는가?
    # - 여기서는 HTTP 요청 자체는 정상 처리되었다.
    # - 단, 장비 상태가 미연결이므로 Body 안에 ERROR_NOT_CONNECTED를 반환하는 구조이다.
    #
    # 즉:
    # - HTTP 200: API 요청 처리 성공
    # - Body ERROR_NOT_CONNECTED: 장비 상태 예외 응답
    #
    # 실제 서비스에서는 정책에 따라 400 또는 409를 사용할 수도 있다.
    # 이 프로젝트에서는 기존 MockRobotDevice의 응답 구조와 맞추기 위해 200 + Error Body로 검증한다.
    assert response.status_code == 200

    # Response Body가 기대한 Error Response인지 확인한다.
    #
    # response.json()은 API 응답 Body를 Python 딕셔너리로 변환한다.
    #
    # 기대값:
    # {
    #   "motor_status": "ERROR_NOT_CONNECTED"
    # }
    #
    # 이 값이 READY로 나오면 문제가 있다.
    # 왜냐하면 장비를 연결하지 않았는데 정상 상태처럼 보이면 안 되기 때문이다.
    assert response.json() == {
        "motor_status": "ERROR_NOT_CONNECTED"
    }