# ============================================================
# app/api_server.py
# ============================================================
#
# 이 파일은 FastAPI 기반 Mock Robot API Server를 정의하는 파일이다.
#
# 기존 구조:
# - app/device.py 안에 있는 MockRobotDevice 클래스를 pytest 테스트에서 직접 호출했다.
# - 예: device.connect(), device.read_motor_status()
#
# 이번 API 자동화 구조:
# - MockRobotDevice 기능을 API endpoint 형태로 감싼다.
# - pytest 테스트는 내부 함수를 직접 호출하지 않고,
#   GET /health, GET /version, GET /motor/status 같은 API를 호출해서 응답을 검증한다.
#
# QA 관점 의미:
# - 실제 서버나 장비 제어 SW가 있는 것처럼 API 응답을 검증하는 구조를 만든다.
# - Health Check, Version Check, Motor Status Check를 Smoke Test 항목으로 자동화할 수 있다.
# ============================================================


# fastapi 패키지에서 FastAPI 클래스를 가져온다.
#
# FastAPI는 Python으로 REST API를 만들 수 있게 해주는 프레임워크이다.
#
# 여기서 REST API는 쉽게 말하면,
# 다른 프로그램이나 테스트 코드가 HTTP 주소를 통해 기능을 호출할 수 있게 만든 통로이다.
#
# 예:
# - GET /health
# - GET /version
# - GET /motor/status
#
# 이 프로젝트에서는 실제 운영 서버를 만들려는 목적이 아니라,
# QA 자동화 테스트에서 API 응답을 검증하기 위한 Mock API Server로 사용한다.
from fastapi import FastAPI


# app/device.py 파일에 정의되어 있는 MockRobotDevice 클래스를 가져온다.
#
# MockRobotDevice는 어디에 있는가?
# - app/device.py 파일 안에 정의되어 있다.
#
# 왜 가져오는가?
# - 기존에 pytest로 직접 검증하던 장비 기능을 API 내부에서도 사용하기 위해서이다.
#
# 기존 테스트 방식:
# - 테스트 코드에서 MockRobotDevice 객체를 직접 생성
# - device.connect()
# - device.read_motor_status()
# - assert로 결과 검증
#
# API 테스트 방식:
# - API 함수 안에서 MockRobotDevice 객체를 생성
# - API 함수 안에서 connect(), read_motor_status() 호출
# - pytest는 API 응답값을 검증
#
# 즉, 이 import는 기존 Mock Device 검증 구조를
# REST API 검증 구조로 확장하기 위해 필요하다.
from app.device import MockRobotDevice


# FastAPI()를 실행해서 API 애플리케이션 객체를 생성한다.
#
# app은 무엇인가?
# - FastAPI 서버의 중심 객체이다.
# - 앞으로 등록할 API 주소들은 모두 이 app 객체에 연결된다.
#
# 왜 필요한가?
# - @app.get("/health") 같은 코드는 app 객체가 있어야 사용할 수 있다.
# - app 객체가 없으면 FastAPI가 어떤 API를 등록해야 하는지 알 수 없다.
#
# 중요한 순서:
# - app = FastAPI()가 먼저 선언되어야 한다.
# - 그 다음에 @app.get(...) 데코레이터를 사용할 수 있다.
#
# 만약 순서가 바뀌면?
# - Python이 @app.get(...)을 읽는 시점에 app이 아직 없기 때문에
#   NameError: name 'app' is not defined 에러가 발생한다.
app = FastAPI()


# ------------------------------------------------------------
# GET /health API
# ------------------------------------------------------------
#
# @app.get("/health")는 데코레이터라고 부른다.
#
# 이 코드는 무슨 뜻인가?
# - GET 방식으로 /health 주소가 호출되면
# - 바로 아래에 있는 health_check() 함수를 실행하라는 의미이다.
#
# 이 함수는 어디에서 호출되는가?
# - 테스트 코드에서 client.get("/health")를 실행하면 호출된다.
# - 즉, tests/smoke/test_api_smoke.py의 API Smoke Test에서 호출한다.
#
# 왜 /health API를 만드는가?
# - 서버나 장비 제어 서비스가 기본적으로 살아 있는지 확인하기 위해서이다.
#
# QA 관점:
# - /health는 Smoke Test에 적합하다.
# - 이유는 후속 테스트를 하기 전에 API 서비스가 정상 응답하는지 먼저 확인해야 하기 때문이다.
@app.get("/health")
def health_check():
    # 이 함수는 GET /health API가 호출되었을 때 실행된다.
    #
    # 왜 이 함수를 쓰는가?
    # - API 서버가 정상 상태인지 알려주는 응답을 만들기 위해서이다.
    #
    # return 뒤의 딕셔너리는 API 응답 Body가 된다.
    # FastAPI는 Python 딕셔너리를 자동으로 JSON 응답으로 변환한다.
    #
    # Python 딕셔너리:
    # {"status": "ok"}
    #
    # 실제 API JSON 응답:
    # {
    #   "status": "ok"
    # }
    #
    # 테스트에서는 이 응답값이 기대값과 같은지 검증한다.
    return {
        "status": "ok"
    }


# ------------------------------------------------------------
# GET /version API
# ------------------------------------------------------------
#
# @app.get("/version")는 GET /version 요청이 들어왔을 때
# 바로 아래 version_check() 함수를 실행하라는 의미이다.
#
# 이 함수는 어디에서 호출되는가?
# - 테스트 코드에서 client.get("/version")를 실행하면 호출된다.
# - 즉, tests/smoke/test_api_smoke.py의 version API 테스트에서 호출한다.
#
# 왜 /version API를 만드는가?
# - 현재 서버 또는 장비 제어 SW의 버전 정보를 확인하기 위해서이다.
#
# QA 관점:
# - 실제 검증 업무에서는 테스트 대상 빌드가 맞는지 확인하는 것이 중요하다.
# - 잘못된 버전으로 테스트하면 테스트 결과 자체의 신뢰도가 떨어진다.
# - 그래서 version check는 Smoke Test에 포함하기 좋다.
@app.get("/version")
def version_check():
    # 이 함수는 GET /version API가 호출되었을 때 실행된다.
    #
    # 왜 이 함수를 쓰는가?
    # - API를 통해 현재 Mock Robot API의 버전 정보를 반환하기 위해서이다.
    #
    # 여기서는 실제 빌드 버전을 읽는 구조가 아니라,
    # 학습용 Mock API이기 때문에 고정값 "1.0.0"을 반환한다.
    #
    # 실제 업무에서는 이 값이 다음과 연결될 수 있다.
    # - 서버 빌드 버전
    # - 장비 Firmware 버전
    # - 배포된 SW 버전
    #
    # 테스트에서는 {"version": "1.0.0"} 응답이 오는지 검증한다.
    return {
        "version": "1.0.0"
    }


# ------------------------------------------------------------
# GET /motor/status API
# ------------------------------------------------------------
#
# @app.get("/motor/status")는 GET /motor/status 요청이 들어왔을 때
# 바로 아래 motor_status_check() 함수를 실행하라는 의미이다.
#
# 이 함수는 어디에서 호출되는가?
# - 테스트 코드에서 client.get("/motor/status")를 실행하면 호출된다.
# - 즉, tests/smoke/test_api_smoke.py의 motor status API 테스트에서 호출한다.
#
# 왜 /motor/status API를 만드는가?
# - 장비의 모터 상태가 정상 준비 상태인지 API로 확인하기 위해서이다.
#
# 기존 구조:
# - pytest 테스트가 MockRobotDevice.read_motor_status()를 직접 호출했다.
#
# 이번 구조:
# - API 내부에서 MockRobotDevice.read_motor_status()를 호출한다.
# - pytest는 API 응답으로 전달된 motor_status 값을 검증한다.
#
# QA 관점:
# - 장비 연결 후 Motor 상태가 READY인지 확인하는 것은 기본 정상 동작 검증이다.
# - 따라서 /motor/status는 API Smoke Test 항목으로 적합하다.
@app.get("/motor/status")
def motor_status_check():
    # MockRobotDevice 객체를 생성한다.
    #
    # MockRobotDevice는 어디에 정의되어 있는가?
    # - app/device.py 파일에 정의되어 있다.
    #
    # 왜 여기서 객체를 생성하는가?
    # - /motor/status API가 호출될 때 테스트용 장비 객체를 준비하기 위해서이다.
    #
    # 이 객체는 실제 로봇 장비를 대신하는 Mock 객체이다.
    # 실제 장비 없이도 연결 상태, 모터 상태, 예외 응답 등을 테스트할 수 있다.
    device = MockRobotDevice()

    # device.connect()를 호출한다.
    #
    # connect()는 어디에 정의되어 있는가?
    # - app/device.py 안의 MockRobotDevice 클래스에 정의되어 있다.
    #
    # 왜 connect()를 호출해야 하는가?
    # - MockRobotDevice는 연결되지 않은 상태에서 motor status를 읽으면
    #   ERROR_NOT_CONNECTED 같은 예외 응답을 반환한다.
    #
    # 이 API는 Smoke Test용 정상 경로를 검증하는 API이다.
    # 따라서 먼저 장비를 연결 상태로 만들어야 한다.
    #
    # 연결 상태가 되어야 read_motor_status() 호출 시 READY를 기대할 수 있다.
    device.connect()

    # device.read_motor_status()를 호출한다.
    #
    # read_motor_status()는 어디에 정의되어 있는가?
    # - app/device.py 안의 MockRobotDevice 클래스에 정의되어 있다.
    #
    # 왜 호출하는가?
    # - 현재 장비의 모터 상태를 읽기 위해서이다.
    #
    # 이 함수의 기대 동작:
    # - 장비가 연결되어 있으면 "READY" 반환
    # - 장비가 연결되어 있지 않으면 "ERROR_NOT_CONNECTED" 반환
    #
    # 위에서 device.connect()를 먼저 호출했기 때문에,
    # 여기서는 motor_status 값이 "READY"가 될 것으로 기대한다.
    motor_status = device.read_motor_status()

    # API 응답 Body를 반환한다.
    #
    # motor_status 변수에는 read_motor_status() 결과가 들어 있다.
    # 연결된 상태에서는 "READY"가 들어갈 것으로 기대한다.
    #
    # FastAPI는 아래 딕셔너리를 JSON 응답으로 변환한다.
    #
    # 실제 API JSON 응답 예:
    # {
    #   "motor_status": "READY"
    # }
    #
    # 테스트에서는 이 응답값이 기대값과 같은지 검증한다.
    return {
        "motor_status": motor_status
    }