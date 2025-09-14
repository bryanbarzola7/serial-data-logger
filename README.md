# Serial Data Logger

Serial Data Logger is a Python tool for collecting data from a serial port (like an Arduino or microcontroller) and saving it to a CSV file. It can also generate a simple plot of the logged data for quick visualization.

> "Data is the new oil, but only if you know how to refine it."

## Features

- **Real‑time logging:** Reads continuous data from a serial port and writes it to a CSV file.
- **Configurable port settings:** Set the COM port and baud rate directly from the command line.
- **Automatic timestamping:** Adds a timestamp column to each sample for easy correlation.
- **Simple plotting:** Generates a Matplotlib line plot of a selected column after logging ends.
- **Cross‑platform:** Works on Windows, macOS, and Linux.

## Getting Started

1. Clone this repository.
2. Install the required dependency:

    pip install pyserial matplotlib

3. Connect your microcontroller or sensor to your computer and determine the serial port (e.g., `COM3` or `/dev/ttyUSB0`).
4. Run the data logger:

    python data_logger.py --port COM3 --baud 9600 --output readings.csv --plot-column value

This will create a CSV file with timestamp and data columns and then display a simple plot for the selected column.

## CSV Format

Each row in the output CSV file includes:
- `timestamp` – the wall‑clock time when the sample was received.
- One or more data values as sent over the serial connection, separated by commas.

## Sample Code

    import serial
    import csv
    from datetime import datetime

    with serial.Serial('COM3', 9600) as ser, open('readings.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'value'])
        while True:
            line = ser.readline().decode().strip()
            writer.writerow([datetime.now().isoformat(), line])

---

For more details on using the `pyserial` library, see the [PySerial documentation](https://pyserial.readthedocs.io/en/latest/).

![Serial Cable](https://images.pexels.com/photos/1103566/pexels-photo-1103566.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200)
