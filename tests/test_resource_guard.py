from core.resource_guard import ResourceGuard


def main():
    guard = ResourceGuard(
        "config/safety_policy.json"
    )

    print("NOVIS Resource Guard Test")
    print("========================")

    normal_snapshot = {
        "system": {
            "cpu_percent": 10,
            "ram_percent": 50,
            "ram_available_gb": 16,
            "battery_percent": 90,
            "plugged_in": True,
        },
        "gpu": {
            "name": "NVIDIA GeForce RTX 2050",
            "temperature_c": 45,
            "gpu_percent": 10,
            "memory_used_mb": 500,
            "memory_total_mb": 4096,
            "power_w": 7,
            "power_limit_w": None,
        },
    }

    hot_gpu_snapshot = {
        **normal_snapshot,
        "gpu": {
            **normal_snapshot["gpu"],
            "temperature_c": 85,
        },
    }

    low_battery_snapshot = {
        **normal_snapshot,
        "system": {
            **normal_snapshot["system"],
            "battery_percent": 15,
            "plugged_in": False,
        },
    }

    normal = guard.evaluate(
        normal_snapshot,
        heavy_ai=True
    )

    hot_gpu = guard.evaluate(
        hot_gpu_snapshot,
        heavy_ai=True
    )

    low_battery = guard.evaluate(
        low_battery_snapshot,
        heavy_ai=True
    )

    print("\nNormal hardware:")
    print(normal["status"])

    print("\nHot GPU:")
    print(hot_gpu["status"])

    print("\nLow battery:")
    print(low_battery["status"])

    passed = (
        normal["status"] == "SAFE"
        and hot_gpu["status"] == "BLOCKED"
        and low_battery["status"] == "BLOCKED"
    )

    print("\n------------------------")

    if passed:
        print("RESULT: RESOURCE SAFETY TEST PASSED")
    else:
        print("RESULT: RESOURCE SAFETY TEST FAILED")


if __name__ == "__main__":
    main()