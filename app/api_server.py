# fastapi 패키지에서 FastAPI 클래스를 가져온다.
# FastAPI는 Python으로 REST API를 만들 수 있게 해주는 프레임워크이다.
# 여기서는 실제 운영 서버가 아니라, QA 자동화 테스트용 Mock API Server로 사용한다.
from fastapi import FastAPI


# FastAPI()를 실행해서 API 애플리케이션 객체를 생성한다.
# 이 app 객체가 있어야 @app.get("/health"), @app.get("/version") 같은 API 주소를 등록할 수 있다.
# 중요: @app.get(...)보다 반드시 먼저 선언되어야 한다.
app = FastAPI()


# @app.get("/health")는 GET /health 요청이 들어왔을 때
# 바로 아래 health_check 함수를 실행하라는 의미이다.
#
# QA 관점에서 /health API는 서버 또는 장비 제어 서비스가 살아 있는지 확인하는
# 가장 기본적인 Smoke Test 항목이다.
@app.get("/health")
def health_check():
    # /health API가 호출되면 이 함수가 실행된다.
    # return 값은 FastAPI가 자동으로 JSON 응답으로 변환한다.
    return {
        "status": "ok"
    }


# @app.get("/version")는 GET /version 요청이 들어왔을 때
# 바로 아래 version_check 함수를 실행하라는 의미이다.
#
# QA 관점에서 /version API는 현재 서버 또는 장비 제어 SW의 버전 정보를 확인하는 Smoke Test 항목이다.
# 실제 검증 업무에서도 배포된 빌드 버전이 맞는지 확인할 때 자주 사용된다.
@app.get("/version")
def version_check():
    # /version API가 호출되면 이 함수가 실행된다.
    # 여기서는 Mock API이므로 고정된 버전값을 반환한다.
    return {
        "version": "1.0.0"
    }