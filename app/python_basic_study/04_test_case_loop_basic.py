# 04_test_case_loop_basic.py

# ------------------------------------------------------------
# 1. 테스트 케이스 목록 만들기
# ------------------------------------------------------------
# test_cases는 여러 개의 테스트 케이스를 담는 리스트이다.
# 리스트 안에는 딕셔너리 형태의 테스트 케이스가 여러 개 들어간다.
#
# 리스트(List): 여러 개의 값을 순서대로 담는 구조
# 딕셔너리(Dictionary): key와 value로 의미 있는 데이터를 묶는 구조
#
# QA 관점:
# 여러 테스트 케이스를 하나의 목록으로 관리하기 위한 구조이다.


test_cases = [
    {
        "test_id" : "TC_001",
        "device_status" : "ready",
        "expected_status" : "ready",
        "battery_level" : 85,
        "expected_min_battery": 50
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
# 2. 테스트 케이스를 하나씩 실행하기
# ------------------------------------------------------------
# for문은 리스트 안에 있는 값을 하나씩 꺼내서 반복 실행한다.
#
# for test_case in test_cases:
#
# 의미:
# test_cases 리스트 안에 있는 테스트 케이스를 하나씩 꺼내서
# 매번 test_case라는 변수 이름으로 사용한다.
#
# in 의미:
# "~ 안에 있는 것 중에서 하나씩 꺼낸다" 라는 뜻이다.

for test_case in test_cases :
    print("-----------------------------------------")
    print("실행 테스트 ID:", test_case["test_id"])


# --------------------------------------------------------
# 3. 상태값 검증
# --------------------------------------------------------
# 딕셔너리에서 실제 상태값과 기대 상태값을 꺼낸다.
# test_case["device_status"]는 현재 테스트 케이스의 실제 상태값이다.
# test_case["expected_status"]는 현재 테스트 케이스의 기대 상태값이다.

    actual_status = test_case["device_status"]
    expected_status = test_case["expected_status"]

    print("기대 상태값:", expected_status)
    print("실제 상태값:", actual_status)

    assert actual_status == expected_status

    print("상태값 검증 Pass")


# --------------------------------------------------------
# 4. 배터리 기준 검증
# --------------------------------------------------------
# 딕셔너리에서 실제 배터리 수치와 최소 기준값을 꺼낸다.
# 실제 배터리 수치가 최소 기준 이상이면 PASS,
# 최소 기준보다 낮으면 AssertionError로 FAIL 처리된다.

    actual_battery = test_case["battery_level"]
    expected_min_battery = test_case["expected_min_battery"]

    print("배터리 최소 기준:", expected_min_battery)
    print("실제 배터리 수치:", actual_battery)

    assert actual_battery >= expected_min_battery

    print("배터리 검증 Pass")

print("-----------------------------------------")
print("All test cases completed")

