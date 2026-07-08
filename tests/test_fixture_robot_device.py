import pytest
from app.device import MockRobotDevice


# ============================================================
# fixture 1: 연결된 Mock Robot Device를 준비하는 fixture
# ============================================================
# @pytest.fixture는 pytest에게 아래 함수를 "테스트 준비 함수"로 등록한다는 뜻이다.
# 즉, 테스트 함수에서 robot_device라는 이름을 사용하면
# pytest가 이 함수를 먼저 실행한 뒤 return 값을 테스트 함수에 전달한다.
@pytest.fixture
def robot_device():
    # MockRobotDevice 객체를 생성한다.
    # QA 관점에서는 테스트 전에 사용할 Mock 장비를 준비하는 단계이다.
    #
    # MockRobotDevice는 app/device.py 파일 안에 정의되어 있는 클래스이다.
    # 쉽게 말하면 "가짜 로봇 장비 설계도"라고 볼 수 있다.
    #
    # 아래 코드는 MockRobotDevice 설계도로 실제 테스트용 장비 객체를 하나 생성하는 코드이다.
    # device 변수를 생성하고, device라는 변수에 MockRobotDevice 장비 객체를 넣는다.
    device = MockRobotDevice()

    # MockRobotDevice()가 실행되면 device.py 안의 __init__() 함수가 자동으로 실행된다.
    #
    # __init__() 안에는 아래와 같은 초기 상태가 정의되어 있다.
    # self.connected = False
    # self.version = "1.0.0"
    # self.motor_status = "READY"
    # self.emergency_stop = False
    #
    # 따라서 장비 객체를 처음 생성한 직후에는 connected 값이 False이다.
    # 즉, 아직 장비가 연결되지 않은 상태이다.

    # 테스트 시작 전에 장비 연결 동작을 수행한다.
    # connect() 함수는 connected 값을 True로 변경하는 역할을 한다
    # connect() 함수 안에는 self.connected = True 코드가 있기 때문에,
    # device.connect()를 실행하면 connected 값이 False에서 True로 변경된다.
    #
    # QA 관점에서는 테스트 전에 장비를 Connect 상태로 Setup 하는 단계이다.
    device.connect()

    # return은 함수가 만든 결과를 밖으로 돌려주는 것이다.
    # 준비가 완료된 device 객체를 테스트 함수에 전달한다.
    #
    # 테스트 함수에서는 이 return된 device 객체를 robot_device라는 이름으로 받아서 사용한다.
    return device


# ============================================================
# fixture 2: 연결하지 않은 Mock Robot Device를 준비하는 fixture
# ============================================================
# 이 fixture는 일부러 device.connect()를 실행하지 않는다.
# 이유는 "장비가 연결되지 않았을 때 에러 처리가 정상적으로 되는지" 검증하기 위해서이다.
@pytest.fixture
def robot_device_not_connected():
    # MockRobotDevice 객체를 생성한다.
    # 이 순간 __init__() 함수가 자동으로 실행된다.
    #
    # __init__() 안에서 self.connected = False로 정의되어 있기 때문에
    # 장비는 아직 연결되지 않은 상태이다.
    device = MockRobotDevice()

    # 여기서는 일부러 device.connect()를 호출하지 않는다.
    #
    # 따라서 현재 상태는 아래와 같다.
    # device.connected = False
    #
    # 이 상태에서 read_motor_status()를 실행하면
    # device.py 로직에 따라 "ERROR_NOT_CONNECTED"가 반환되어야 한다.
    return device


# ============================================================
# Test Case 1: fixture가 장비를 연결 상태로 준비했는지 검증
# ============================================================
def test_robot_device_connection_with_fixture(robot_device):
    # fixture에서 전달받은 robot_device 객체의 현재 연결 상태를 확인한다.
    # connect()가 실행되면 device.py 내부에서 connected 값이 True로 변경된다.

    # 동작 Flow
    # 1. pytest가 test_robot_device_connection_with_fixture 테스트를 실행하려고 한다.
    # 2. 테스트 함수 괄호 안에 robot_device가 있는 것을 확인한다.
    # 3. pytest는 같은 이름의 fixture인 robot_device()를 먼저 실행한다.
    # 4. robot_device fixture 안에서 MockRobotDevice 객체를 생성한다.
    # 5. robot_device fixture 안에서 device.connect()를 실행한다.
    # 6. fixture가 return한 device 객체를 이 테스트 함수에 전달한다.
    # 7. 테스트 함수는 전달받은 robot_device로 연결 상태를 검증한다.

    # Mock 장비의 현재 연결 상태를 actual_connected 변수에 저장한다.
    #
    # robot_device.connected는 Mock 장비의 현재 연결 상태를 의미한다.
    #
    # fixture에서 device.connect()를 실행했기 때문에
    # connected 값은 True가 되어야 한다.
    #
    # actual_connected는 실제 결과값이다.
    actual_connected = robot_device.connected

    # 기대하는 장비 연결 상태값을 정의한다.
    #
    # expected_connected는 기대 결과값이다.
    # 장비가 연결된 상태를 기대하므로 True로 정의한다.
    expected_connected = True

    # 실제 연결 상태와 기대 연결 상태를 비교하여 PASS / FAIL을 판정한다.
    #
    # assert는 PASS / FAIL을 판정하는 문법이다.
    #
    # actual_connected와 expected_connected가 같으면 PASS
    # 다르면 FAIL
    #
    # 현재 기대 흐름은 아래와 같다.
    # actual_connected = True
    # expected_connected = True
    # 따라서 assert True == True가 되어 PASS가 되어야 한다.
    assert actual_connected == expected_connected


# ============================================================
# Test Case 2: 연결된 장비의 motor_status가 READY인지 검증
# ============================================================
def test_robot_device_motor_status_with_fixture(robot_device):
    # fixture에서 전달받은 robot_device 객체의 모터 상태를 확인한다.
    #
    # 이 테스트도 robot_device fixture를 사용한다.
    #
    # 따라서 테스트 시작 전에 아래 동작이 이미 수행된 상태이다.
    # 1. MockRobotDevice 객체 생성
    # 2. device.connect() 실행
    # 3. connected 값이 True로 변경
    # 4. 준비된 device 객체가 테스트 함수에 전달됨

    # read_motor_status()는 device.py 안에 정의되어 있는 함수이다.
    #
    # device.py의 read_motor_status() 로직은 다음과 같다.
    #
    # if not self.connected:
    #     return "ERROR_NOT_CONNECTED"
    # return self.motor_status
    #
    # 현재는 fixture에서 device.connect()를 실행했기 때문에 connected 값은 True이다.
    # 따라서 "ERROR_NOT_CONNECTED"가 아니라 self.motor_status 값이 반환되어야 한다.
    #
    # read_motor_status()는 연결된 상태라면 motor_status 값을 반환한다.
    # actual_status는 실제 모터 상태 결과값이다.
    actual_status = robot_device.read_motor_status()

    # device.py에서 motor_status 기본값은 "READY"로 정의되어 있다.
    #
    # self.motor_status = "READY"
    #
    # 따라서 연결된 상태에서 read_motor_status()를 실행하면
    # 기대 결과는 "READY"이다.
    expected_status = "READY"

    # 실제 모터 상태와 기대 모터 상태를 비교한다.
    #
    # actual_status = "READY"
    # expected_status = "READY"
    #
    # 두 값이 같으면 PASS이다.
    assert actual_status == expected_status


# ============================================================
# Test Case 3: 연결하지 않은 장비에서 motor_status를 읽으면 에러가 나오는지 검증
# ============================================================
def test_robot_device_motor_status_without_connection(robot_device_not_connected):
    # 이 테스트는 robot_device_not_connected fixture를 사용한다.
    #
    # robot_device_not_connected fixture는 MockRobotDevice 객체만 생성하고
    # device.connect()를 일부러 실행하지 않는다.
    #
    # 따라서 현재 장비 상태는 아래와 같다.
    #
    # connected = False
    #
    # QA 관점에서는 "장비가 연결되지 않은 상태에서 기능을 호출했을 때
    # 올바른 에러 메시지가 나오는지" 확인하는 예외 테스트이다.

    # 연결되지 않은 장비에서 모터 상태를 읽는다.
    #
    # read_motor_status() 함수는 connected 값이 False이면
    # "ERROR_NOT_CONNECTED"를 반환하도록 구현되어 있다.
    #
    # actual_status는 실제 결과값이다.
    actual_status = robot_device_not_connected.read_motor_status()

    # 연결되지 않은 상태에서 기대하는 결과값이다.
    #
    # 정상 모터 상태인 "READY"가 아니라,
    # 연결되지 않았다는 에러 메시지인 "ERROR_NOT_CONNECTED"가 나와야 한다.
    expected_status = "ERROR_NOT_CONNECTED"

    # 실제 결과와 기대 결과를 비교한다.
    #
    # actual_status = "ERROR_NOT_CONNECTED"
    # expected_status = "ERROR_NOT_CONNECTED"
    #
    # 두 값이 같으면 PASS이다.
    assert actual_status == expected_status