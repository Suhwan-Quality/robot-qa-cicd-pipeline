class MockRobotDevice:
    def __init__(self):
        self.connected = False
        self.version = "1.0.0"
        self.motor_status = "READY"
        self.emergency_stop = False

    def connect(self):
        self.connected = True
        return "CONNECTED"

    def read_version(self):
        if not self.connected:
            return "ERROR_NOT_CONNECTED"
        return self.version

    def read_motor_status(self):
        if not self.connected:
            return "ERROR_NOT_CONNECTED"
        return self.motor_status

    def read_emergency_stop_status(self):
        if not self.connected:
            return "ERROR_NOT_CONNECTED"
        return self.emergency_stop

    def send_command(self, command):
        if not self.connected:
            return "ERROR_NOT_CONNECTED"

        if command == "INVALID_COMMAND":
            return "ERROR_INVALID_COMMAND"

        return "OK"