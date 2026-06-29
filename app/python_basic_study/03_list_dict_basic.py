# 03_list_dict_basic.py

# ------------------------------------------------------------
# 1. 리스트(List) 기초
# ------------------------------------------------------------
# 리스트는 여러 개의 값을 하나로 묶어서 저장하는 자료형이다.
# QA 자동화에서는 여러 상태값, 테스트 입력값, 테스트 케이스 목록을 관리할 때 사용한다.

device_status_list = ["ready", "error", "disconnected"]

print("장비 상태 목록:", device_status_list)


# ------------------------------------------------------------
# 2. for 반복문으로 리스트 값 하나씩 확인
# ------------------------------------------------------------
# for 반복문은 리스트 안에 있는 값을 하나씩 꺼내서 처리할 때 사용한다.
# 아래 코드는 device_status_list에 들어 있는 상태값을 하나씩 출력한다.

for status in device_status_list :
    print("현재 상태값:", status)


# ------------------------------------------------------------
# 3. 딕셔너리(Dictionary) 기초
# ------------------------------------------------------------
# 딕셔너리는 key와 value 형태로 데이터를 저장한다.
# QA 자동화에서는 장비 이름, 상태값, 배터리 수치, 연결 여부처럼
# 하나의 테스트 대상 정보를 묶어서 관리할 때 유용하다.

device_info = {
    "device_name": "Mock Robot Device",
    "device_status": "ready",
    "battery_level": 85,
    "is_connected": True
}

print("장비 이름:", device_info["device_name"])
print("장비 상태:", device_info["device_status"])
print("배터리 수치:", device_info["battery_level"])
print("연결 여부:", device_info["is_connected"])

# ------------------------------------------------------------
# 4. 딕셔너리 값을 사용한 상태값 검증
# ------------------------------------------------------------
# 딕셔너리에서 실제 상태값을 꺼내고,
# 기대 상태값과 비교하여 PASS / FAIL을 판정한다.

expected_status = "ready"
actual_status = device_info["device_status"]

print("기대 상태값:", expected_status)
print("실제 상태값:", actual_status)

assert actual_status == expected_status

print("Dictionary status check passed")