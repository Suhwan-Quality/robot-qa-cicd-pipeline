# 05_test_result_summary_basic.py

# ------------------------------------------------------------
# 1. 테스트 케이스 목록 만들기
# ------------------------------------------------------------
# test_cases는 여러 개의 테스트 케이스를 담는 리스트이다.
# 리스트 안의 각 딕셔너리는 하나의 테스트 케이스를 의미한다.
#
# QA 관점:
# 여러 테스트 케이스를 하나의 목록으로 관리하고,
# for문으로 하나씩 실행하기 위한 구조이다.


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
        "battery_level" : 20,
        "expected_min_battery" : 50
    }
]

# ------------------------------------------------------------
# 2. 테스트 결과 개수 저장 변수
# ------------------------------------------------------------
# pass_count는 PASS된 테스트 개수를 저장한다.
# fail_count는 FAIL된 테스트 개수를 저장한다.
#
# 처음에는 아무 테스트도 실행하지 않았으므로 0으로 시작한다.

pass_count = 0
fail_count = 0


# ------------------------------------------------------------
# 3. 테스트 케이스 반복 실행
# ------------------------------------------------------------
# for문은 test_cases 리스트 안의 테스트 케이스를 하나씩 꺼낸다.
#
# for test_case in test_cases:
#
# 의미:
# test_cases 안에 있는 딕셔너리 하나를 꺼내서
# 그 값을 test_case라는 이름으로 사용한다.

for test_case in test_cases :
    print("---------------------------------")
    print("실행 테스트 ID", test_case["test_id"])

    # --------------------------------------------------------
    # 4. try-except 구조
    # --------------------------------------------------------
    # try 안에는 실제 검증 코드를 넣는다.
    # 검증 중 AssertionError가 발생하면 except 쪽으로 이동한다.
    #
    # QA 관점:
    # 테스트가 실패하더라도 프로그램을 완전히 멈추지 않고,
    # FAIL로 기록한 뒤 다음 테스트를 계속 실행하기 위한 구조이다.

    

    # ----------------------------------------------------
    # 5. 상태값 검증
    # ----------------------------------------------------
    # 딕셔너리에서 실제 상태값과 기대 상태값을 꺼낸다.
    try :
        actual_status = test_case["device_status"]
        expected_status = test_case["expected_status"]

        print("기대 상태값:", expected_status)
        print("실제 상태값:", actual_status)

        #실제 상태값과 기대 상태값이 같아야 Pass 이다.
        assert actual_status == expected_status

        print("상태값 검증 Pass")

        # ----------------------------------------------------
        # 6. 배터리 기준 검증
        # ----------------------------------------------------
        # 딕셔너리에서 실제 배터리 수치와 최소 기준값을 꺼낸다.

        actual_battery = test_case["battery_level"]
        expected_min_battery = test_case["expected_min_battery"]

        print("배터리 최소 기준:", expected_min_battery)
        print("실제 배터리 수치:", actual_battery)

        # 실제 배터리 수치가 최소 기준 이상이어야 Pass 이다.
        assert actual_battery >= expected_min_battery

        print("배터리 검증 Pass")

        # 여기까지 왔다는것은 상태값 검증과 배터리 검증이 모두 통과했다는 것이다.
        print("테스트 결과 : Pass")

        # Pass개수를 1개 증가시킨다.
        pass_count = pass_count + 1

    except AssertionError : 
        # assert 검증에서 실패하면 이쪽으로 이동한다.
        # 즉, 테스트 조건을 만족하지 못한 Fail 케이스 이다.

        print("테스트 결과 : Fail")

        # Fail 개수를 1개 증가 시킨다.
        fail_count = fail_count +1


# ------------------------------------------------------------
# 7. 전체 테스트 결과 요약 출력
# ------------------------------------------------------------
# 모든 테스트 케이스 실행이 끝난 뒤,
# 전체 개수 / PASS 개수 / FAIL 개수를 출력한다.

print("-----------------------------------")
print("전체 테스트 케이스 수:", len(test_cases))
print("Pass 개수:", pass_count)
print("Fail 개수:", fail_count)
print("All test cases completed")