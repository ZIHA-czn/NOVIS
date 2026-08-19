from pathlib import Path
from core.safety import SafetyCore


POLICY_PATH = Path(__file__).parent.parent / "config" / "safety_policy.json"


def main():
    safety = SafetyCore(str(POLICY_PATH))

    checks = {
        "computer_control": False,
        "autonomous_action": False,
        "self_modification": False,
        "privilege_escalation": False,
        "network_action": False,
    }

    print("NOVIS Safety Core Test")
    print("-" * 30)

    all_passed = True

    for action, expected in checks.items():
        result = safety.is_allowed(action)

        status = "PASS" if result == expected else "FAIL"

        print(f"{action:22} {status}")

        if result != expected:
            all_passed = False

    print("-" * 30)

    safety.emergency_stop()

    emergency_result = safety.is_allowed("computer_control")

    if emergency_result is False:
        print("emergency_stop         PASS")
    else:
        print("emergency_stop         FAIL")
        all_passed = False

    print("-" * 30)

    if all_passed:
        print("RESULT: ALL SAFETY TESTS PASSED")
    else:
        print("RESULT: SAFETY TEST FAILED")


if __name__ == "__main__":
    main()