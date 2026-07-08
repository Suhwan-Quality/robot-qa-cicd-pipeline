# ============================================================
# 07_function_parameter_basic.py
# 함수의 괄호 (), 인자(parameter), return 기초 이해
# ============================================================
#
# 이 파일의 목적:
# pytest fixture에서 def robot_device(): 괄호 안이 왜 비어 있는지,
# 테스트 함수에서는 왜 def test_xxx(robot_device, should_connect, expected_status): 처럼
# 괄호 안에 값이 들어가는지 이해하기 위한 기초 연습이다.


# ============================================================
# 1. 값을 받지 않는 함수
# ============================================================
# 아래 함수는 괄호 안이 비어 있다.
# 
# make_ready_status라는 함수를 만든다.
# 이 함수는 실행되면 "READY" 값을 밖으로 돌려준다.
#
# def make_ready_status():
#
# 이유:
# 이 함수는 외부에서 어떤 값을 받을 필요가 없기 때문이다.
#
# 함수 안에서 직접 "READY"라는 값을 만들어서 return 한다.
def make_ready_status():
    # return은 함수가 만든 결과를 밖으로 돌려주는 문법이다.
    #
    # 이 함수는 실행되면 항상 "READY"라는 값을 돌려준다.
    return "READY"


# ============================================================
# 2. 값을 받는 함수
# ============================================================
# 아래 함수는 괄호 안에 actual_status가 들어 있다.
#
# 설명: 
# check_status라는 함수를 만든다.
# 이 함수는 actual_status라는 값을 외부에서 받아야 한다.
# 함수 안에서 expected_status 변수에 "READY"를 저장한다.
# 그리고 actual_status와 expected_status가 같은지 assert로 비교한다.
#
# def check_status(actual_status):
#
# 이유:
# 이 함수는 actual_status라는 실제 결과값을 외부에서 받아야 검증할 수 있기 때문이다.
#
# 즉, 이 함수는 혼자서는 검증할 값이 없다.
# 밖에서 actual_status 값을 넣어줘야 한다.
def check_status(actual_status):

    # expected_status는 기대 결과값이다.
    # QA에서 expected는 "나와야 하는 값"을 의미한다.
    expected_status = "READY"

    # actual_status는 실제 결과값이다.
    # 이 값은 함수 괄호 안으로 전달받은 값이다.
    #
    # assert는 actual_status와 expected_status를 비교한다.
    # 같으면 PASS처럼 정상 진행되고,
    # 다르면 AssertionError가 발생한다.
    assert actual_status == expected_status


    # ============================================================
    # 3. 함수 실행 흐름
    # ============================================================

    # make_ready_status() 함수 실행
    #
    # make_ready_status()는 값을 받지 않는 함수이므로
    # 괄호 안에 아무것도 넣지 않는다.
    #
    # 이 함수는 "READY"를 return 한다.
    status = make_ready_status()
    # 위 코드는 실제로 이렇게 이해하면 된다.
    # status라는 변수를 만들고,
    # 그 안에 make_ready_status()가 돌려준 "READY" 값을 저장한다.
    #
    # status = "READY"
    #
    # 즉, make_ready_status()가 돌려준 "READY" 값이
    # status 변수에 저장된다.

    # check_status(status) 함수 실행
    #
    # check_status()는 actual_status 값을 받아야 하는 함수이다.
    #
    # 그래서 괄호 안에 status를 넣어준다.
    #
    # 현재 status 변수 안에는 "READY"가 들어 있다.
    #
    # 따라서 check_status(status)는 실제로 아래와 비슷하게 동작한다.
    #
    # check_status("READY")
    check_status(status)

    # 여기까지 에러가 없으면 아래 문장이 출력된다.
    # 즉, actual_status와 expected_status가 같아서 검증이 통과했다는 뜻이다.
    print("status 값:", status)
    print("PASS: 함수 인자와 return 기본 검증 성공")


    # 전체 설명
    # make_ready_status 함수를 만든다.
    # 이 함수는 실행되면 "READY" 값을 반환한다.
    # check_status 함수를 만든다.
    # 이 함수는 actual_status라는 값을 외부에서 받아서 사용한다.
    # 함수 안에서 expected_status 변수를 만들고 "READY" 값을 저장한다.
    # 그리고 assert를 사용해서 actual_status와 expected_status를 비교한다.
    # 
    # status = make_ready_status()를 실행하면
    # make_ready_status 함수가 "READY"를 반환하고,
    # 그 반환값이 status 변수에 저장된다.
    # 
    # check_status(status)를 실행하면
    # status 변수 안에 들어있는 "READY" 값이
    # check_status 함수의 actual_status로 전달된다.
    # 
    # 그 결과 actual_status는 "READY",
    # expected_status도 "READY"가 되어
    # assert actual_status == expected_status 검증이 통과한다.
