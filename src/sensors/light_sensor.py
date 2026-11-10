"""LM393 light module for simple black-line detection.

The module's potentiometer sets the light/dark threshold. It reports only a
digital state, not brightness or distance from the line.
"""

from gpiozero import DigitalInputDevice


class LightSensor:
    def __init__(self, cfg: dict):
        """Set up the sensor using ``light_sensor_pin`` in the config.

        Set ``line_detected_high`` to True if the module's digital output is
        HIGH over the black line; otherwise leave it False (the default).
        Check the actual module output during calibration.
        """
        pin = int(cfg['light_sensor_pin'])
        line_detected_high = cfg.get('line_detected_high', False)
        self.device = DigitalInputDevice(
            pin,
            pull_up=True,
            active_state=bool(line_detected_high),
        )

    def is_line_detected(self) -> bool:
        """Return True when the configured output level indicates the line."""
        return self.device.is_active

    def close(self):
        """Release the GPIO pin."""
        self.device.close()


"""
Test mode 
from time import sleep

from sensors.light_sensor import LightSensor


sensor = LightSensor({
    "light_sensor_pin": 17,       # BCM GPIO numbering; physical pin 11
    "line_detected_high": False,  # Change after observing/calibrating the output
})

try:
    while True:
        print("Line detected:", sensor.is_line_detected())
        sleep(0.2)
except KeyboardInterrupt:
    pass
finally:
    sensor.close()



"""