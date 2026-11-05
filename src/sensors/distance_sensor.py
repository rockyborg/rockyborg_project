"""VL53L1X ToF: non-blocking sample polling, returned in centimetres."""
import time


class DistanceSensor:
    def __init__(self, i2c, cfg: dict):
        import adafruit_vl53l1x
        self.device = adafruit_vl53l1x.VL53L1X(i2c, address=int(cfg.get('tof_address', '0x29'), 0))
        self.device.distance_mode = int(cfg.get('tof_distance_mode', 1))
        self.device.timing_budget = int(cfg.get('tof_timing_budget_ms', 50))
        self.last_cm = None
        self.last_at = 0.0
        self.device.start_ranging()

    def poll(self):
        """Returns the last valid fresh range; caller checks age separately."""
        if self.device.data_ready:
            try:
                distance = self.device.distance  # Adafruit's API returns centimetres
                if distance is not None and distance > 0:
                    self.last_cm = float(distance)
                    self.last_at = time.monotonic()
                else:
                    self.last_cm = None
                    self.last_at = 0.0
            finally:
                self.device.clear_interrupt()

    def distance_cm(self, max_age_s=0.75):
        if time.monotonic() - self.last_at > max_age_s:
            return None
        return self.last_cm

    def close(self):
        self.device.stop_ranging()
