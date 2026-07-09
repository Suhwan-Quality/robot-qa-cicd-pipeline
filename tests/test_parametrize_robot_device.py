import pytest


# pytest.mark.parametrize는
# 하나의 테스트 함수에 여러 조건 데이터를 넣어
# 같은 검증 로직을 반복 실행하게 해주는 pytest 기능이다.
#
# QA 실무 관점에서는
# 테스트 케이스를 복붙하지 않고
# 조건표 기반으로 여러 입력/기대값을 관리할 수 있다.
@pytest.mark.parametrize(
    "should_connect, expected_status",
    [
        # Case 1.
        # 장비가 연결되지 않은 상태에서는
        # 모터 상태가 ERROR_NOT_CONNECTED로 응답해야 한다.
        (False, "ERROR_NOT_CONNECTED"),

        # Case 2.
        # 장비가 연결된 상태에서는
        # 모터 상태가 READY로 응답해야 한다.
        (True, "READY"),
    ]
)
def test_motor_status_by_connection_state(robot_device, should_connect, expected_status):
    # robot_device는 tests/conftest.py에 정의된 공통 fixture이다.
    # pytest는 테스트 실행 시 conftest.py를 자동으로 인식해서
    # 이 테스트 함수에 MockRobotDevice 객체를 전달한다.

    # should_connect 값이 True인 경우에만 장비를 연결한다.
    if should_connect:
        robot_device.connect()

    # 실제 모터 상태를 읽는다.
    actual_status = robot_device.read_motor_status()

    # 기대 결과와 실제 결과가 같은지 검증한다.
    assert actual_status == expected_status