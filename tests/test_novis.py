from core.novis import Novis


def main():
    novis = Novis()

    print("NOVIS Emergency Stop Test")
    print("=========================")

    print("Before stop:")
    print("running:", novis.running)

    novis.emergency_stop()

    print("\nAfter stop:")
    print("running:", novis.running)

    allowed = novis.can_start_heavy_ai()

    print("heavy AI allowed:", allowed)

    if novis.running is False and allowed is False:
        print("\nRESULT: EMERGENCY STOP PASSED")
    else:
        print("\nRESULT: EMERGENCY STOP FAILED")


if __name__ == "__main__":
    main()