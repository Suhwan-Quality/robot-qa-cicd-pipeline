# 06_quality_gate_basic.py
# ------------------------------------------------------------
# 1. 테스트 케이스 목록 만들기
# ------------------------------------------------------------
# test_cases는 여러 개의 테스트 케이스를 담는 리스트이다.
# 리스트 안의 각 딕셔너리는 하나의 테스트 케이스를 의미한다.
#
# [] 대괄호:
# 여러 테스트 케이스를 하나의 목록으로 묶기 위해 사용한다.
#
# {} 중괄호:
# 하나의 테스트 케이스 정보를 key/value 형태로 묶기 위해 사용한다.
#
# QA 관점:
# 여러 테스트 케이스를 관리하고, 반복 실행하기 위한 테스트


test_cases = [
    {
        "test_id" : "TC_001",
        "device_status" : "ready",
        "expected_status" : "ready",
        "battery_level" : 85,
        "expected_min_battery" : 50
    },
    {
        "test_id" : "TC_002",
        "device_status" : "ready",
        "expected_status" : "ready",
        "battery_level" : 50,
        "expected_min_battery" : 50  
    },
    {
        "test_id" : "TC_003",
        "device_status" : "ready",
        "expected_status" : "ready",
        "battery_level" : 85,
        "expected_min_battery" : 50  
    }
]

# ------------------------------------------------------------
# 2. 테스트 결과 개수 저장 변수
# ------------------------------------------------------------
# pass_count는 PASS된 테스트 개수를 저장한다.
# fail_count는 FAIL된 테스트 개수를 저장한다.
#
# 테스트 실행 전에는 아직 결과가 없으므로 0으로 시작한다.

pass_count = 0
fail_count = 0


# ------------------------------------------------------------
# 3. 테스트 케이스 반복 실행
# ------------------------------------------------------------
# for문은 test_cases 리스트 안의 테스트 케이스를 하나씩 꺼내서 실행한다.
#
# for test_case in test_cases:
#
# 의미:
# test_cases 안에 있는 딕셔너리 하나를 꺼내서
# 매번 test_case라는 변수 이름으로 사용한다.
#
# in:
# "~ 안에 있는 값 중에서 하나씩 꺼낸다"는 의미이다.

for test_case in test_cases :
    print("------------------------------------")
    print("실제 테스트 ID:", test_case["test_id"])

    # --------------------------------------------------------
    # 4. try-except로 테스트 실패 처리
    # --------------------------------------------------------
    # try:
    #   검증 코드를 실행하는 영역이다.
    #
    # except AssertionError:
    #   assert 검증이 실패했을 때 실행되는 영역이다.
    #
    # QA 관점:
    # 특정 테스트가 실패해도 전체 실행을 멈추지 않고,
    # FAIL로 기록한 뒤 다음 테스트를 계속 실행하기 위해 사용한다.

    try : 
        # ----------------------------------------------------
        # 5. 상태값 검증
        # ----------------------------------------------------
        # 현재 테스트 케이스 딕셔너리에서 실제 상태값과 기대 상태값을 꺼낸다.

        actual_status = test_case["device_status"]
        expected_status = test_case["expected_status"]

        print("기대 상태값:", expected_status)
        print("실제 상태값:", actual_status)

        # 실제 상태값과 기대 상태값이 같아야 Pass이다.
        assert actual_status == expected_status

        print("상태값 검증 Pass")


        # ----------------------------------------------------
        # 6. 배터리 기준 검증
        # ----------------------------------------------------
        # 현재 테스트 케이스 딕셔너리에서 실제 배터리 수치와 최소 기준값을 꺼낸다.

        actual_battery = test_case["battery_level"]
        expected_min_battery = test_case["expected_min_battery"]

        print("배터리 최소 기준:", expected_min_battery)
        print("실제 배터리 수치:", actual_battery)

        # 실제 배터리 수치가 최소 기준 이상이어야 Pass이다.
        assert actual_battery >= expected_min_battery

        print("배터리 검증 Pass")

        # 상태값 검증과 배터리 검증이 모두 통과하면 테스트 결과는 PASS이다.
        print("테스트 결과 : Pass")

        # Pass 개수를 1 증가 시킨다.
        pass_count = pass_count + 1
    
    except AssertionError :
        # assert 조건을 만족하지 못하면 이쪽으로 이동한다.
        # 즉, 해당 테스트 케이스는 FAIL이다.

        print("테스트 결과 : Fail")

        # Fail 개수를 1 증가시킨다.
        fail_count = fail_count + 1


# ------------------------------------------------------------
# 7. 전체 테스트 결과 요약 출력
# ------------------------------------------------------------
# len(test_cases)는 전체 테스트 케이스 개수를 의미한다.
# len()은 리스트 안에 값이 몇 개 있는지 세는 함수이다.

print("--------------------------------------")
print("전체 테스트 케이스 수:", len(test_cases))
print("Pass 개수", pass_count)
print("Fail 개수:", fail_count)


# ------------------------------------------------------------
# 8. Quality Gate 판정
# ------------------------------------------------------------
# Quality Gate는 테스트 결과를 기준으로 최종 진행 여부를 판단하는 기준이다.
#
# if fail_count == 0:
#   FAIL이 하나도 없으면 GO
#
# else:
#   FAIL이 하나라도 있으면 NO-GO
#
# QA 관점:
# 자동화 테스트 결과를 기반으로 릴리즈 가능 여부를 판단하는 구조이다.

if fail_count == 0 :
    quality_gate_result = "Go"

else : 
    quality_gate_result = "No-Go"

print("Quality Gate 결과:", quality_gate_result)


# ------------------------------------------------------------
# 9. Quality Gate 결과 파일 저장
# ------------------------------------------------------------
# open()은 파일을 열 때 사용하는 함수이다.
#
# "reports/quality_gate_basic.txt":
#   저장할 파일 경로이다.
#
# "w":
#   write의 의미이며, 파일에 새로 쓰겠다는 뜻이다.
#
# encoding="utf-8":
#   한글이 깨지지 않도록 하기 위한 설정이다.
#
# with:
#   파일을 열고 사용한 뒤 자동으로 닫아주는 구조이다.
#
# QA 관점:
# CI/CD 실행 결과로 Quality Gate 결과 파일을 남기기 위한 구조이다.

with open("reports/quality_gate_basic.txt", "w", encoding="utf-8") as file:

    # 파일 첫 줄에 제목을 작성한다.
    # \n은 줄바꿈을 의미한다.
    file.write("Quality Gate Result\n")

    # 결과 파일에서 제목과 내용 구분을 위해 구분선을 작성한다.
    file.write("-------------------\n")

    # 전체 테스트 케이스 수를 파일에 저장한다.
    # len(test_cases)는 test_cases 리스트 안에 들어있는 테스트 케이스 개수를 의미한다.
    # len(test_cases)의 결과는 숫자이므로, 파일에 쓰기 위해 str()로 문자열로 변환한다.
    # + 는 문자열끼리 이어 붙이는 역할을 한다.
    file.write("Total Test Cases: " + str(len(test_cases)) + "\n")

    # PASS된 테스트 케이스 개수를 파일에 저장한다.
    # pass_count는 숫자이므로 str(pass_count)로 문자열 변환 후 저장한다.
    file.write("PASS Count: " + str(pass_count) + "\n")

    # FAIL된 테스트 케이스 개수를 파일에 저장한다.
    # fail_count는 숫자이므로 str(fail_count)로 문자열 변환 후 저장한다.
    file.write("FAIL Count: " + str(fail_count) + "\n")

    # 최종 Quality Gate 결과를 파일에 저장한다.
    # quality_gate_result는 "GO" 또는 "NO-GO" 문자열 값이다.
    file.write("Quality Gate: " + quality_gate_result + "\n")


print("Quality Gate 결과 파일 저장 완료")
print("All test cases completed")