from app.device import MockRobotDevice


def test_invalid_command_returns_error():
    device = MockRobotDevice()
    device.connect()

    response = device.send_command("INVALID_COMMAND")

    assert response == "ERROR_INVALID_COMMAND"


def test_read_version_without_connection():
    device = MockRobotDevice()

    version = device.read_version()

    assert version == "ERROR_NOT_CONNECTED"


def test_motor_status_without_connection():
    device = MockRobotDevice()

    motor_status = device.read_motor_status()

    assert motor_status == "ERROR_NOT_CONNECTED"


def test_emergency_stop_status_without_connection():
    device = MockRobotDevice()

    emergency_stop = device.read_emergency_stop_status()

    assert emergency_stop == "ERROR_NOT_CONNECTED"