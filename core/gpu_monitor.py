import subprocess


class GPUMonitor:
    def get_snapshot(self):
        command = [
            "nvidia-smi",
            "--query-gpu=name,temperature.gpu,utilization.gpu,memory.used,memory.total,power.draw,power.limit",
            "--format=csv,noheader,nounits",
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5,
            check=True,
        )

        values = [value.strip() for value in result.stdout.strip().split(",")]

        def to_number(value):
            if value in ("[N/A]", "N/A", ""):
                return None
            return float(value)

        return {
            "name": values[0],
            "temperature_c": to_number(values[1]),
            "gpu_percent": to_number(values[2]),
            "memory_used_mb": to_number(values[3]),
            "memory_total_mb": to_number(values[4]),
            "power_w": to_number(values[5]),
            "power_limit_w": to_number(values[6]),
        }


if __name__ == "__main__":
    monitor = GPUMonitor()

    print("NOVIS GPU Monitor")
    print("-----------------")

    snapshot = monitor.get_snapshot()

    for name, value in snapshot.items():
        print(f"{name:20} {value}")