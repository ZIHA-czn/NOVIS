# NOVIS

NOVIS is a safety-first personal AI assistant project for Windows.

## Current Status

Early development.

Current foundation:

- Safety Core
- Emergency Stop
- CPU and RAM monitoring
- Battery monitoring
- NVIDIA GPU monitoring
- Resource Guard
- Hardware safety checks
- Automated safety tests

## Safety

NOVIS currently prevents:

- Uncontrolled computer control
- Autonomous actions
- Self-modification
- Privilege escalation
- Network actions

NOVIS also uses resource and hardware safeguards to reduce unnecessary system load.

## Resource Safety

The current configuration includes limits for:

- CPU usage
- RAM usage
- GPU usage
- GPU temperature
- Battery level

Heavy AI workloads are disabled while the laptop is running on battery.

## Hardware

Development machine:

- Intel Core i7-1355U
- 32 GB RAM
- NVIDIA GeForce RTX 2050 4 GB VRAM
- Windows 11
- Python 3.11

## Project Structure

NOVIS/
  config/
    safety_policy.json
  core/
    safety.py
    hardware_monitor.py
    gpu_monitor.py
    system_monitor.py
    resource_guard.py
    novis.py
  tests/
    test_safety.py
    test_novis.py
    test_resource_guard.py

## Safety First

NOVIS is being developed incrementally.

Safety systems are implemented and tested before adding higher-level capabilities.

Potentially impactful capabilities remain disabled until they are explicitly designed, tested, and approved.

## Development

This project is currently under active development.

More capabilities will be added gradually after safety and resource checks are established.

## License

License to be decided.
