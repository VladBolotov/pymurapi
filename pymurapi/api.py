import time


class MurApiBase(object):
    """Base class for AUV and Simulator API."""

    def __init__(self):
        self.depth = 0.0
        self.yaw = 0.0
        self.pitch = 0.0
        self.roll = 0.0
        self.temperature = 0.0
        self.pressure = 0.0
        self.voltage = 0.0

        self.is_thrust_in_ms = False
        self.colorRGB = [0, 30, 0]
        self.motors_power = [0, 0, 0, 0, 0, 0, 0, 0]
        self.on_delay = 1.5
        self.off_delay = 0.7

    @staticmethod
    def _dirty_wait():
        """Prevent freezes on some PC. Fix needed"""
        time.sleep(0.0005)

    def _prepare(self):
        pass

    def _update(self):
        pass

    def get_image_front(self):
        """Returns front image. SIMULATOR ONLY!"""
        pass

    def get_image_bottom(self):
        """Returns bottom image. SIMULATOR ONLY!"""
        pass

    def set_on_delay(self, value):
        """Set LED ON delay. If value set to 0 LED will be always OFF"""
        self._dirty_wait()
        self.on_delay = value

    def set_off_delay(self, value):
        """Set LED OFF delay. If value set to 0 LED will be always ON"""
        self._dirty_wait()
        self.off_delay = value

    def set_rgb_color(self, r, g, b):
        """Set LED color in RGB colorspace. Values are 0 - 255"""
        self._dirty_wait()
        self.colorRGB = [int(r), int(g), int(b)]

    def set_motor_power(self, motor_id, power):
        """Set motor (motor_id 0 - 8) power. Values can be between 2 ** 15 and -2 ** 15 if thrust in ms enabled.
           Values can be between 100 and -100 if thrust in ms disabled.
        """
        self._dirty_wait()
        if motor_id < 0 or motor_id > 8:
            return
        if abs(power) > 32767:
            return
        self.motors_power[int(motor_id)] = int(power)

    def set_enable_power_in_ms(self, enabled):
        """Set power in ms mode enabled(True)  or disabled(False)"""
        self._dirty_wait()
        self.is_thrust_in_ms = enabled

    def get_depth(self):
        """Returns current depth in meters."""
        self._dirty_wait()
        return self.depth

    def get_yaw(self):
        """Returns current yaw in degrees from -180 to 180"""
        self._dirty_wait()
        return self.yaw

    def get_pitch(self):
        """Returns current pitch in degrees from -180 to 180."""
        self._dirty_wait()
        return self.pitch

    def get_roll(self):
        """Returns current roll in degrees from -180 to 180."""
        self._dirty_wait()
        return self.roll

    def get_temperature(self):
        """Returns current temperature in Celsius."""
        self._dirty_wait()
        return self.temperature

    def get_pressure(self):
        """Returns current outer pressure in Pascals."""
        self._dirty_wait()
        return self.pressure

    def get_voltage(self):
        """Returns current voltage in volts. i.e. 12.3"""
        self._dirty_wait()
        return self.voltage
