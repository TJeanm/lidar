# RPLIDAR Scan Reader

A minimal Python experiment for reading scans from an RPLIDAR connected over USB serial. The script prints device information, health status, and each incoming scan; it stops and disconnects the sensor when interrupted.

## Requirements

- A compatible RPLIDAR and access to its serial device.
- Python 3 and a package that provides `from rplidar import RPLidar`.
- Permission to read the serial port.

The port is currently set to `/dev/ttyUSB0` in [`lier.py`](lier.py). Change `PORT_NAME` if your device appears at another path.

## Run

```bash
python3 lier.py
```

Press `Ctrl+C` to stop the scan loop. The script calls `stop()` and `disconnect()` in its cleanup block.

## Scope

This repository contains one hardware test script. It does not process point clouds, map an environment, or provide a simulated LiDAR source. Its purpose is to confirm basic communication and inspect raw scan output.
