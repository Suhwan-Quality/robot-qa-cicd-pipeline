# 이 파일은 pytest fixture를 사용해서 MockRobotDevice를 검증하는 테스트 파일입니다.
# fixture는 테스트마다 반복되는 준비 과정을 공통으로 처리할 때 사용합니다.

# 이 파일에서는 pytest를 직접 import하지 않습니다.
# 이유는 robot_device fixture를 이 파일 안에서 만들지 않고,
# tests/conftest.py에 있는 공통 fixture를 pytest가 자동으로 찾아서 사용하기 때문입니다.


def test_robot_device_connection_with_fixture(robot_device):
    # def는 Python에서 함수를 만들 때 사용하는 키워드입니다.
    # pytest는 함수 이름이 test_로 시작하면 자동으로 테스트 케이스로 인식합니다.

    # 함수 괄호 안의 robot_device는 tests/conftest.py에 정의한 fixture 이름입니다.
    # pytest는 이 이름을 보고 conftest.py의 robot_device fixture를 자동으로 실행합니다.

    # robot_device.connect()는 MockRobotDevice를 연결 상태로 변경하는 동작입니다.
    # QA 관점에서는 "장비 연결 기능이 정상 동작하는지" 확인하는 준비 단계입니다.
    robot_device.connect()

    # robot_device.connected는 장비가 연결되었는지 확인하는 상태값입니다.
    # 이전에 robot_device.is_connected라고 작성했지만,
    # 실제 MockRobotDevice 클래스에는 is_connected가 없고 connected가 있습니다.
    # 그래서 실제 코드에 존재하는 connected를 사용해야 합니다.

    # assert는 실제 결과가 기대 결과와 같은지 확인하는 검증 문장입니다.
    # connected 값이 True이면 테스트는 PASS입니다.
    # connected 값이 True가 아니면 테스트는 FAIL입니다.
    assert robot_device.connected is True


def test_robot_device_motor_status_with_fixture(robot_device):
    # 이 테스트는 장비가 연결된 상태에서 모터 상태가 READY인지 확인합니다.
    # 정상 시나리오, 즉 Smoke Test 성격에 가까운 검증입니다.

    # 먼저 장비를 연결합니다.
    # 연결하지 않으면 모터 상태가 READY가 아니라 ERROR_NOT_CONNECTED가 될 수 있습니다.
    robot_device.connect()

    # read_motor_status()는 현재 모터 상태를 읽어오는 함수입니다.
    # 이전에 get_motor_status()라고 작성했지만,
    # 실제 MockRobotDevice 클래스에는 get_motor_status()가 없고 read_motor_status()가 있습니다.
    # 그래서 실제 코드에 존재하는 read_motor_status()를 사용해야 합니다.
    actual_status = robot_device.read_motor_status()

    # expected_status는 우리가 기대하는 결과값입니다.
    # 장비가 정상 연결되었으므로 모터 상태는 READY가 되어야 합니다.
    expected_status = "READY"

    # 실제 결과(actual_status)와 기대 결과(expected_status)를 비교합니다.
    # 두 값이 같으면 PASS, 다르면 FAIL입니다.
    assert actual_status == expected_status


def test_robot_device_motor_status_without_connection(robot_device):
    # 이 테스트는 장비를 연결하지 않은 상태에서 모터 상태를 확인합니다.
    # 정상 케이스가 아니라 예외/부정 경로 검증입니다.
    # QA에서는 이런 테스트를 Negative Test 또는 Regression Test로 많이 봅니다.

    # 여기서는 일부러 robot_device.connect()를 호출하지 않습니다.
    # 즉, 장비가 연결되지 않은 상태를 재현합니다.

    # 연결되지 않은 상태에서 모터 상태를 조회합니다.
    # 실제 MockRobotDevice 클래스에 맞춰 read_motor_status()를 사용합니다.
    actual_status = robot_device.read_motor_status()

    # 연결되지 않았으므로 기대 결과는 ERROR_NOT_CONNECTED입니다.
    expected_status = "ERROR_NOT_CONNECTED"

    # 실제 결과가 기대한 에러 상태와 같은지 검증합니다.
    # 이 테스트는 "비정상 상황에서도 시스템이 올바른 에러를 반환하는지" 확인합니다.
    assert actual_status == expected_status