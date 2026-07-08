# pytest 기능을 사용하기 위해 pytest를 import 한다.
# import는 Python에서 외부 기능이나 라이브러리를 현재 파일에서 사용하겠다는 뜻이다.
# 여기서는 pytest의 parametrize 기능을 사용하기 위해 필요하다.
import pytest

# ============================================================
# pytest parametrize 기본 실습
# ============================================================
# parametrize는 하나의 테스트 함수에 여러 테스트 데이터를 넣어서
# 같은 검증 로직을 여러 번 반복 실행하게 해주는 pytest 기능이다.
#
# QA 관점에서 보면:
# expected / actual 비교 로직은 동일한데,
# 검증해야 할 데이터만 여러 개일 때 사용하면 좋다.
#
# 예를 들어 아래 3가지 상태값을 검증한다고 가정한다.
#
# 1. READY == READY
# 2. CONNECTED == CONNECTED
# 3. ERROR_NOT_CONNECTED == ERROR_NOT_CONNECTED
#
# 이걸 테스트 함수 3개로 따로 만들 수도 있지만,
# parametrize를 사용하면 테스트 함수 1개로 3개 케이스를 반복 검증할 수 있다.


# ------------------------------------------------------------
# @pytest.mark.parametrize 설명
# ------------------------------------------------------------
# @pytest.mark.parametrize는 pytest에게 이렇게 알려주는 역할이다.
#
# "아래 테스트 함수에 여러 개의 테스트 데이터를 넣어서 반복 실행해라."
#
# 즉, 아래 test_device_status_with_parametrize 함수는 코드상으로는 1개지만,
# parametrize 안에 데이터가 3개 있기 때문에 pytest가 총 3번 실행한다.

@pytest.mark.parametrize(
    # --------------------------------------------------------
    # 첫 번째 인자: "actual_status, expected_status"
    # --------------------------------------------------------
    # 여기에는 테스트 함수로 전달할 변수 이름을 적는다.
    #
    # actual_status:
    # 실제 결과값을 담을 변수 이름이다.
    #
    # expected_status:
    # 기대 결과값을 담을 변수 이름이다.
    #
    # 이 이름들은 아래 테스트 함수의 괄호 안에 있는 이름과 반드시 같아야 한다.
    #
    # 아래쪽 테스트 함수:
    # def test_device_status_with_parametrize(actual_status, expected_status):
    #
    # 여기 이름과 위 이름이 서로 연결된다.
    "actual_status, expected_status",

    # --------------------------------------------------------
    # 두 번째 인자: 테스트 데이터 목록
    # --------------------------------------------------------
    # [] 대괄호는 Python에서 리스트를 만들 때 사용한다.
    #
    # 리스트는 여러 개의 데이터를 순서대로 담는 상자라고 생각하면 된다.
    #
    # 여기서는 테스트 데이터를 3개 넣었다.
    [
        # ----------------------------------------------------
        # 첫 번째 테스트 데이터
        # ----------------------------------------------------
        # () 소괄호 안에 값이 2개 들어 있다.
        #
        # 첫 번째 값 "READY"는 actual_status 변수로 들어간다.
        # 두 번째 값 "READY"는 expected_status 변수로 들어간다.
        #
        # 즉 1회차 테스트에서는 아래처럼 동작한다.
        #
        # actual_status = "READY"
        # expected_status = "READY"
        ("READY", "READY"),


        # ----------------------------------------------------
        # 두 번째 테스트 데이터
        # ----------------------------------------------------
        # 2회차 테스트에서는 아래처럼 동작한다.
        #
        # actual_status = "CONNECTED"
        # expected_status = "CONNECTED"
        ("CONNECTED", "CONNECTED"),


        # ----------------------------------------------------
        # 세 번째 테스트 데이터
        # ----------------------------------------------------
        # 3회차 테스트에서는 아래처럼 동작한다.
        #
        # actual_status = "ERROR_NOT_CONNECTED"
        # expected_status = "ERROR_NOT_CONNECTED"
        #
        # 이 데이터는 예외 상황 메시지 검증 예시로 볼 수 있다.
        # 예를 들어 장비가 연결되지 않은 상태에서 기능을 호출했을 때
        # ERROR_NOT_CONNECTED가 나와야 한다는 식의 검증에 사용할 수 있다.
        ("ERROR_NOT_CONNECTED", "ERROR_NOT_CONNECTED"),
    ]
)

# ============================================================
# Test Case: 여러 상태값을 parametrize로 반복 검증
# ============================================================
# pytest는 test_로 시작하는 함수를 테스트 함수로 인식한다.
#
# 이 함수는 코드상으로는 1개이지만,
# 위의 @pytest.mark.parametrize에 테스트 데이터가 3개 있기 때문에
# pytest가 이 함수를 3번 반복 실행한다.

def test_device_status_with_parametrize(actual_status, expected_status):
    # --------------------------------------------------------
    # 이 테스트 함수가 실행되는 흐름
    # --------------------------------------------------------
    #
    # 1. pytest가 test_parametrize_basic.py 파일을 찾는다.
    # 2. test_device_status_with_parametrize 테스트 함수를 찾는다.
    # 3. 함수 위에 @pytest.mark.parametrize가 있는 것을 확인한다.
    # 4. parametrize 안에 테스트 데이터가 3개 있는 것을 확인한다.
    # 5. 같은 테스트 함수를 3번 반복 실행한다.
    #
    # 실행 예시:
    #
    # 1회차:
    # actual_status = "READY"
    # expected_status = "READY"
    #
    # 2회차:
    # actual_status = "CONNECTED"
    # expected_status = "CONNECTED"
    #
    # 3회차:
    # actual_status = "ERROR_NOT_CONNECTED"
    # expected_status = "ERROR_NOT_CONNECTED"

    # --------------------------------------------------------
    # actual_status 설명
    # --------------------------------------------------------
    # actual_status는 실제 결과값이다.
    #
    # QA에서 actual은 "실제 결과"를 의미한다.
    # 즉, 장비나 프로그램에서 실제로 나온 값을 의미한다.
    #
    # 이번 예제에서는 실제 장비를 호출하는 단계는 아니고,
    # parametrize 데이터에서 첫 번째 값이 actual_status로 들어온다.

    # --------------------------------------------------------
    # expected_status 설명
    # --------------------------------------------------------
    # expected_status는 기대 결과값이다.
    #
    # QA에서 expected는 "기대 결과"를 의미한다.
    # 즉, 요구사항이나 테스트 케이스상 나와야 하는 값을 의미한다.
    #
    # 이번 예제에서는 parametrize 데이터에서 두 번째 값이 expected_status로 들어온다.

    # --------------------------------------------------------
    # assert 설명
    # --------------------------------------------------------
    # assert는 pytest에서 PASS / FAIL을 판정할 때 사용하는 문법이다.
    #
    # assert actual_status == expected_status
    #
    # 이 뜻은:
    #
    # actual_status 값과 expected_status 값이 같으면 PASS
    # actual_status 값과 expected_status 값이 다르면 FAIL
    #
    # 여기서 == 는 "두 값이 같은지 비교한다"는 뜻이다.
    #
    # 주의:
    # =  는 값을 변수에 저장할 때 사용한다.
    # == 는 두 값이 같은지 비교할 때 사용한다.
    #
    # 예:
    # actual_status = "READY"
    # → actual_status 변수에 "READY" 값을 저장
    #
    # actual_status == expected_status
    # → actual_status와 expected_status가 같은지 비교
    
    assert actual_status == expected_status