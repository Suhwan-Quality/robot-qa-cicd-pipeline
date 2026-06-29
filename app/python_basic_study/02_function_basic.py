# 1. 상태값 검증 함수

def check_device_status(actual_status, expected_status) :
    print("기대 상태값:", expected_status)
    print("실제 상태값:", actual_status)

    assert actual_status == expected_status

    print("Status check passed")

# 2. 배터리 검증 함수

def check_battery_level(actual_battery, expected_min_battery) :
    print("배터리 최소 기준 수치:", expected_min_battery)
    print("실제 배터리 수치:", actual_battery)

    assert actual_battery >= expected_min_battery

    print("Battery check Passed")

# 3. 테스트에 사용할 실제 값

# device_status = "ready"

device_status = "ready"
# device_status는 실제 장비에서 읽어온 상태값이라고 가정한다.
# 여기서는 Fail 케이스 확인을 위해 "error"로 가정한다.

battery_level = 85
# battery_level은 실제 배터리 수치라고 가정한다.
# 배터리 Fail 케이스 확인을 위해 최소 기준보다 낮은 값으로 설정한다

# 4. 함수 실행
#배터리 최소 기준을 50으로 설정하고, 실제 배터리 20이 기준 미달인지 검증한다.
check_device_status(device_status, "ready")
check_battery_level(battery_level, 50)