from app.device import MockRobotDevice

def test_device_connection():
    device = MockRobotDevice()

    result = device.connect()

    assert result == "CONNECTED"


def test_read_version_after_connection():
    device = MockRobotDevice()
    device.connect()

    version = device.read_version()

    assert version == "1.0.0"


def test_motor_status_is_ready():
    device = MockRobotDevice()
    device.connect()

    motor_status = device.read_motor_status()

    assert motor_status == "READY"


def test_emergency_stop_is_false():
    device = MockRobotDevice()
    device.connect()

    emergency_stop = device.read_emergency_stop_status()

    assert emergency_stop is False


def test_invalid_command_returns_error():
    device = MockRobotDevice()
    device.connect()

    response = device.send_command("INVALID_COMMAND")

    assert response == "ERROR_INVALID_COMMAND"


def test_read_version_without_connection():
    device = MockRobotDevice()

    version = device.read_version()

    assert version == "ERROR_NOT_CONNECTED"