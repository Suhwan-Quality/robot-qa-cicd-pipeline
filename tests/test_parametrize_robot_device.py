# pytest 기능을 사용하기 위해 pytest를 import 한다.
# 이번 파일에서는 fixture와 parametrize를 모두 사용할 것이기 때문에 필요하다.
import pytest

# app/device.py 파일 안에 있는 MockRobotDevice 클래스를 가져온다.
# MockRobotDevice는 테스트에 사용할 가짜 로봇 장비 객체이다.
from app.device import MockRobotDevice

# ============================================================
# fixture: MockRobotDevice 객체를 준비하는 fixture
# ============================================================
# @pytest.fixture는 pytest에게 아래 함수를 "테스트 준비 함수"로 등록한다는 뜻이다.
#
# robot_device 라는 함수를 생성한다.
# 테스트 함수에서 robot_device라는 이름을 사용하면,
# pytest가 이 fixture를 먼저 실행한 뒤 return 값을 테스트 함수에 전달한다.
@pytest.fixture
def robot_device():
    
    # MockRobotDevice 객체를 생성한다.
    #
    # MockRobotDevice()가 실행되면 app/device.py 안의 __init__() 함수가 자동으로 실행된다.
    #
    # __init__() 안에는 아래와 같은 초기 상태가 정의되어 있다.
    #
    # self.connected = False
    # self.version = "1.0.0"
    # self.motor_status = "READY"
    # self.emergency_stop = False
    #
    # 따라서 처음 생성된 장비는 아직 연결되지 않은 상태이다.
    device = MockRobotDevice()


    # 여기서는 일부러 device.connect()를 실행하지 않는다.
    #
    # 이유:
    # 이번 테스트에서는 parametrize 데이터를 이용해서
    # 어떤 케이스에서는 connect()를 실행하고,
    # 어떤 케이스에서는 connect()를 실행하지 않을 것이기 때문이다.
    #
    # 즉, 연결 여부를 fixture에서 고정하지 않고
    # 테스트 데이터로 제어하기 위해서이다.
    return device


# ============================================================
# Test Case: 연결 여부에 따른 motor_status 결과를 parametrize로 반복 검증
# ============================================================
# @pytest.mark.parametrize는 하나의 테스트 함수에 여러 테스트 데이터를 넣어
# 같은 검증 로직을 반복 실행하게 해주는 기능이다.
#
# 이번에는 should_connect와 expected_status라는 두 개의 값을 테스트 함수에 전달한다.
#
# should_connect:
# 장비를 연결할지 말지를 결정하는 값이다.
# True이면 device.connect()를 실행한다.
# False이면 device.connect()를 실행하지 않는다.
#
# expected_status:
# read_motor_status()를 실행했을 때 기대하는 결과값이다.
@pytest.mark.parametrize(
    "should_connect, expected_status",
    [
        # ----------------------------------------------------
        # 1번째 테스트 데이터: 장비를 연결하지 않는 케이스
        # ----------------------------------------------------
        # should_connect = False
        # expected_status = "ERROR_NOT_CONNECTED"
        #
        # 장비를 연결하지 않았기 때문에 read_motor_status()를 실행하면
        # 정상 모터 상태인 "READY"가 아니라
        # "ERROR_NOT_CONNECTED"가 나와야 한다.
        (False, "ERROR_NOT_CONNECTED"),


        # ----------------------------------------------------
        # 2번째 테스트 데이터: 장비를 연결하는 케이스
        # ----------------------------------------------------
        # should_connect = True
        # expected_status = "READY"
        #
        # 장비를 연결한 후 read_motor_status()를 실행하면
        # app/device.py의 motor_status 기본값인 "READY"가 나와야 한다.
        (True, "READY"),
    ]
)

def test_motor_status_by_connection_state(robot_device, should_connect, expected_status):
    # --------------------------------------------------------
    # 이 테스트 함수의 실행 흐름
    # --------------------------------------------------------
    #
    # 1. pytest가 이 테스트 함수를 발견한다.
    # 2. 함수 괄호 안에 robot_device가 있는 것을 확인한다.
    # 3. pytest가 robot_device fixture를 먼저 실행한다.
    # 4. fixture는 MockRobotDevice 객체를 생성해서 return한다.
    # 5. pytest가 parametrize 데이터도 확인한다.
    # 6. 첫 번째 데이터로 테스트를 한 번 실행한다.
    # 7. 두 번째 데이터로 테스트를 한 번 더 실행한다.
    #
    # 즉, 이 테스트 함수는 코드상으로는 1개지만 실제로는 2번 실행된다.


    # --------------------------------------------------------
    # should_connect 값에 따라 장비 연결 여부를 결정한다.
    # --------------------------------------------------------
    #
    # if는 Python에서 조건문이다.
    #
    # if should_connect:
    #
    # 이 뜻은:
    # should_connect 값이 True이면 아래 코드를 실행하라는 의미이다.
    #
    # 1번째 테스트에서는 should_connect = False 이므로 connect()를 실행하지 않는다.
    # 2번째 테스트에서는 should_connect = True 이므로 connect()를 실행한다.
    if should_connect:
        # device.connect()를 실행하면 app/device.py 안의 connect(self) 함수가 실행된다.
        #
        # connect() 함수 안에는 아래 코드가 있다.
        #
        # self.connected = True
        # return "CONNECTED"
        #
        # 따라서 connect()를 실행하면 장비 연결 상태가 True로 바뀐다.
        robot_device.connect()


    # --------------------------------------------------------
    # 실제 결과값 확인
    # --------------------------------------------------------
    #
    # read_motor_status()는 app/device.py 안에 정의된 함수이다.
    #
    # device.py의 read_motor_status() 로직은 다음과 같다.
    #
    # if not self.connected:
    #     return "ERROR_NOT_CONNECTED"
    # return self.motor_status
    #
    # 의미:
    # - 장비가 연결되지 않았으면 "ERROR_NOT_CONNECTED" 반환
    # - 장비가 연결되어 있으면 self.motor_status 반환
    #
    # self.motor_status 기본값은 "READY"이다.

    actual_status = robot_device.read_motor_status()


    # --------------------------------------------------------
    # PASS / FAIL 판정
    # --------------------------------------------------------
    #
    # expected_status는 parametrize에서 전달받은 기대 결과값이다.
    #
    # 1번째 테스트:
    # should_connect = False
    # expected_status = "ERROR_NOT_CONNECTED"
    #
    # 2번째 테스트:
    # should_connect = True
    # expected_status = "READY"
    #
    # assert는 실제 결과와 기대 결과를 비교한다.
    #
    # actual_status와 expected_status가 같으면 PASS
    # 다르면 FAIL

    assert actual_status == expected_status