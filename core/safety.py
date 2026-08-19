import json
from pathlib import Path


class SafetyCore:
    def __init__(self, policy_path: str):
        self.policy_path = Path(policy_path)
        self.policy = self._load_policy()
        self.emergency_stopped = False

    def _load_policy(self) -> dict:
        with self.policy_path.open("r", encoding="utf-8-sig") as file:
            return json.load(file)

    def is_allowed(self, action: str) -> bool:
        safety = self.policy["safety"]

        if self.emergency_stopped:
            return False

        if action == "computer_control":
            return safety["computer_control"]

        if action == "autonomous_action":
            return safety["autonomous_actions"]

        if action == "self_modification":
            return safety["self_modification"]

        if action == "privilege_escalation":
            return safety["privilege_escalation"]

        if action == "network_action":
            return safety["network_actions"]

        return False

    def emergency_stop(self) -> None:
        self.emergency_stopped = True

    def reset_emergency_stop(self) -> None:
        self.emergency_stopped = False

    def get_resource_limits(self) -> dict:
        return self.policy["resources"]