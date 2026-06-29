# 01_python_basic.py

# 1. 변수

device_name = "Mock Robot Device"
device_status = "ready"
battery_level = 85
is_connected = True


print("Device Name:", device_name)
print("Device status:", device_status)
print("Battery Level:", battery_level)
print("Connected:", is_connected)

# 2. 조건문

if is_connected == True :
    print("Device is connected")
else : 
    print("Device is not connected")


# 3. 기대값과 실제값 비교

# expected_status = "ready"
# actual_status = device_status

expected_min_battery = 50
actual_battery = battery_level

# print("기대값:", expected_min_battery)
# print("실제값:", actual_battery)

print("배터리 최소 기준 수치:", expected_min_battery)
print("실제 배터리 수치", actual_battery)

# assert actual_battery == expected_min_battery

assert actual_battery >= expected_min_battery

# print("Status check passed")

print("Battery check passed")