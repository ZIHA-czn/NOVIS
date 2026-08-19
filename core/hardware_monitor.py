import psutil
import time


class HardwareMonitor:
    def get_snapshot(self):
        memory = psutil.virtual_memory()
        battery = psutil.sensors_battery()

        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "ram_percent": memory.percent,
            "ram_available_gb": round(memory.available / (1024 ** 3), 2),
            "battery_percent": (
                round(battery.percent, 1)
                if battery is not None
                else None
            ),
            "plugged_in": (
                battery.power_plugged
                if battery is not None
                else None
            ),
        }


if __name__ == "__main__":
    monitor = HardwareMonitor()

    print("NOVIS Hardware Monitor")
    print("----------------------")

    snapshot = monitor.get_snapshot()

    for name, value in snapshot.items():
        print(f"{name:20} {value}")