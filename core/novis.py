from core.safety import SafetyCore
from core.system_monitor import SystemMonitor
from core.resource_guard import ResourceGuard


class Novis:
    def __init__(self):
        self.safety = SafetyCore(
            "config/safety_policy.json"
        )

        self.monitor = SystemMonitor()

        self.guard = ResourceGuard(
            "config/safety_policy.json"
        )

        self.running = True

    def status(self):
        snapshot = self.monitor.get_snapshot()

        safety_result = self.guard.evaluate(
            snapshot,
            heavy_ai=False
        )

        return {
            "running": self.running,
            "safety": safety_result,
            "hardware": snapshot,
        }

    def emergency_stop(self):
        self.safety.emergency_stop()
        self.running = False

    def can_start_heavy_ai(self):
        if not self.running:
            return False

        snapshot = self.monitor.get_snapshot()

        result = self.guard.evaluate(
            snapshot,
            heavy_ai=True
        )

        return result["status"] == "SAFE"


if __name__ == "__main__":
    novis = Novis()

    print("NOVIS Core")
    print("===========")

    status = novis.status()

    print(f"NOVIS running: {status['running']}")
    print(f"Safety status: {status['safety']['status']}")

    if status["safety"]["reasons"]:
        print("\nSafety warnings:")

        for reason in status["safety"]["reasons"]:
            print(f"- {reason}")
    else:
        print("Safety warnings: none")

    print("\nHeavy AI allowed:",
          novis.can_start_heavy_ai())