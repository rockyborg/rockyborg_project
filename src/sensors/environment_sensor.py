"""BME280: ambient temperature in °C, humidity in %RH and pressure in hPa."""


class EnvironmentSensor:
    def __init__(self, i2c, address: str):
        from adafruit_bme280 import basic as bme280
        self.device = bme280.Adafruit_BME280_I2C(i2c, address=int(address, 0))

    def read(self) -> dict:
        return {
            'temperature_c': round(float(self.device.temperature), 2),
            'pressure_hpa': round(float(self.device.pressure), 2),
            'humidity_pct': round(float(self.device.humidity), 2),
        }
