from core.hardware_monitor import HardwareMonitor
from core.gpu_monitor import GPUMonitor


class SystemMonitor:
    def __init__(self):
        self.hardware = HardwareMonitor()
        self.gpu = GPUMonitor()

    def get_snapshot(self):
        return {
            "system": self.hardware.get_snapshot(),
            "gpu": self.gpu.get_snapshot(),
        }


if __name__ == "__main__":
    monitor = SystemMonitor()

    snapshot = monitor.get_snapshot()

    print("NOVIS System Monitor")
    print("====================")

    print("\nSystem")
    print("------")

    for name, value in snapshot["system"].items():
        print(f"{name:20} {value}")

    print("\nGPU")
    print("---")

    for name, value in snapshot["gpu"].items():
        print(f"{name:20} {value}")