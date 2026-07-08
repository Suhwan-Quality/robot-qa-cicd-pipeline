import pytest

@pytest.fixture
def device_status_data() :
    # QA 검증에서 사용할 expected / actual 데이터를 준비한다
    # fixture는 테스트 실행 전에 필요한 준비 데이터를 만들어주는 역할이다.

    return {
        "expected_status" : "READY",
        "actual_status" : "READY",
    }

def test_device_status_with_fixture(device_status_data) : 
    # fixture에서 전달받은 딕셔너리 데이터에서 기대값을 꺼낸다
    expected = device_status_data["expected_status"]

    # fixture에서 전달받은 딕셔너리 데이터에서 실제값을 꺼낸다
    actual = device_status_data["actual_status"]

    # expected / actual 비교를 통해 PASS / FAIL을 판정한다
    assert actual == expected


