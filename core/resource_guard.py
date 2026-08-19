import json
from pathlib import Path


class ResourceGuard:
    def __init__(self, policy_path: str):
        self.policy_path = Path(policy_path)
        self.policy = self._load_policy()

    def _load_policy(self):
        with self.policy_path.open("r", encoding="utf-8-sig") as file:
            return json.load(file)

    def evaluate(self, snapshot: dict, heavy_ai: bool = False) -> dict:
        resources = self.policy["resources"]
        thermal = self.policy["thermal"]
        battery = self.policy["battery"]

        system = snapshot["system"]
        gpu = snapshot["gpu"]

        reasons = []
        status = "SAFE"

        cpu = system["cpu_percent"]
        ram = system["ram_percent"]
        gpu_usage = gpu["gpu_percent"]
        gpu_temp = gpu["temperature_c"]
        battery_percent = system["battery_percent"]
        plugged_in = system["plugged_in"]

        if cpu >= resources["max_cpu_percent"]:
            status = "BLOCKED"
            reasons.append("CPU usage is above the safety limit")

        if ram >= resources["max_ram_percent"]:
            status = "BLOCKED"
            reasons.append("RAM usage is above the safety limit")

        if gpu_usage >= resources["max_gpu_percent"]:
            status = "BLOCKED"
            reasons.append("GPU usage is above the safety limit")

        if gpu_temp >= thermal["gpu_block_c"]:
            status = "BLOCKED"
            reasons.append("GPU temperature is above the safety limit")

        if gpu_temp >= thermal["gpu_caution_c"] and status == "SAFE":
            status = "CAUTION"
            reasons.append("GPU temperature is elevated")

        if (
            battery_percent is not None
            and battery_percent <= battery["caution_percent"]
            and status == "SAFE"
        ):
            status = "CAUTION"
            reasons.append("Battery level is low")

        if heavy_ai:
            if not plugged_in and not resources["heavy_ai_on_battery"]:
                status = "BLOCKED"
                reasons.append("Heavy AI is disabled while on battery")

            if (
                battery_percent is not None
                and battery_percent <= battery["block_heavy_ai_percent"]
            ):
                status = "BLOCKED"
                reasons.append("Battery is too low for heavy AI")

        return {
            "status": status,
            "reasons": reasons,
        }


if __name__ == "__main__":
    from core.system_monitor import SystemMonitor

    monitor = SystemMonitor()
    snapshot = monitor.get_snapshot()

    guard = ResourceGuard(
        "config/safety_policy.json"
    )

    result = guard.evaluate(snapshot, heavy_ai=False)

    print("NOVIS Resource Guard")
    print("====================")
    print(f"Status: {result['status']}")

    if result["reasons"]:
        print("\nReasons:")
        for reason in result["reasons"]:
            print(f"- {reason}")
    else:
        print("No safety warnings.")