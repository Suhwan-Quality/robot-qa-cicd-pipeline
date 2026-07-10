# FastAPI의 TestClient를 가져온다.
# TestClient는 실제 서버를 따로 실행하지 않아도
# 테스트 코드 안에서 API를 호출할 수 있게 해주는 도구이다.
from fastapi.testclient import TestClient


# app/api_server.py 파일에 정의한 app 객체를 가져온다.
# 이 app 객체 안에는 /health API가 등록되어 있다.
from app.api_server import app


# TestClient는 테스트용 API 클라이언트이다.
# client.get("/health")처럼 사용하면 실제 서버를 띄우지 않아도 API를 호출할 수 있다.
# App에 등록된 API를 테스트할 수 있는 Client 객체를 만든다.
client = TestClient(app)


def test_health_api_returns_ok():
    # health API가 ok를 반환하는지 테스트한다
    # GET 방식으로 /health API를 호출한다.
    response = client.get("/health")
    # GET /health API를 호출하고,
    # 그 응답 결과를 response 변수에 저장한다.

    # HTTP Status Code가 200인지 확인한다.
    # 200 → 정상
    # 404 → 주소 없음
    # 500 → 서버 내부 오류
    # 400 → 잘못된 요청
    assert response.status_code == 200

    # 응답 Body가 {"status": "ok"}인지 확인한다.
    # response.json()은 API 응답을 Python 딕셔너리로 바꿔주는 기능
    assert response.json() == {
        "status": "ok"
    }

def test_version_api_returns_version():
    # 이 테스트 함수는 /version API가 정상적으로 버전 정보를 반환하는지 검증한다.
    #
    # QA 테스트 케이스로 보면 아래와 같다.
    #
    # Test Step:
    # - GET /version API 호출
    #
    # Expected Result:
    # - HTTP Status Code가 200이어야 한다.
    # - Response Body에 version 값이 "1.0.0"으로 반환되어야 한다.

    # GET /version API를 호출한다.
    # client.get("/version")는 GET 방식으로 /version API를 호출한다는 뜻이다.
    # 호출 결과는 response 변수에 저장된다.
    response = client.get("/version")

    # response.status_code는 HTTP 응답 상태 코드이다.
    # 200은 API 요청이 정상 처리되었다는 의미이다.
    # 응답 상태 코드가 정상인지 확인한다.
    # 실제 응답 코드가 200이 아니면 pytest가 FAIL 처리한다.
    assert response.status_code == 200

    # response.json()은 API 응답 Body를 Python 딕셔너리 형태로 변환한다.
    #
    # 여기서는 API 응답 Body가 {"version": "1.0.0"}과 정확히 일치하는지 확인한다.
    # 값이 다르거나 key 이름이 다르면 FAIL 처리된다.
    assert response.json() == {
        "version": "1.0.0"
    }