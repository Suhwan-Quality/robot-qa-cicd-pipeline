# pytest 기능을 사용하기 위해 pytest 라이브러리를 가져옵니다.
# 여기서는 @pytest.fixture 기능을 사용하기 위해 필요합니다.
import pytest

# app 폴더 안에 있는 device.py 파일에서 MockRobotDevice 클래스를 가져옵니다.
# MockRobotDevice는 실제 장비 대신 테스트용으로 사용하는 가짜 Robot Device 객체입니다.
from app.device import MockRobotDevice


# @pytest.fixture는 pytest에게 "이 함수는 테스트 준비용 함수입니다"라고 알려주는 표시입니다.
# fixture는 여러 테스트에서 반복해서 사용하는 준비 코드를 공통으로 관리할 때 사용합니다.
@pytest.fixture
def robot_device():
    # 이 함수 이름(robot_device)은 테스트 함수에서 그대로 사용할 수 있습니다.
    # 예: def test_robot_status(robot_device):
    # pytest는 테스트 함수 안의 robot_device 이름을 보고 이 fixture를 자동으로 실행합니다.

    # 아래 설명문은 함수 설명용 주석입니다.
    # 나중에 코드를 보는 사람이 "이 fixture가 왜 필요한지" 이해할 수 있게 적어둡니다.
    """
    MockRobotDevice 테스트에서 공통으로 사용하는 fixture.

    QA 관점:
    - 테스트마다 새로운 MockRobotDevice 객체를 생성합니다.
    - 테스트 간 상태가 섞이는 것을 방지합니다.
    - 반복되는 장비 준비 코드를 conftest.py로 분리합니다.
    - 여러 테스트 파일에서 같은 fixture를 재사용할 수 있습니다.
    """

    # MockRobotDevice 객체를 새로 생성해서 테스트 함수에 전달합니다.
    # return은 "이 값을 함수 밖으로 돌려준다"는 뜻입니다.
    # 즉, 테스트 함수에서 robot_device를 사용하면 이 MockRobotDevice 객체를 받게 됩니다.
    return MockRobotDevice()