import csv
import argparse
import datetime
import sys

try:
    import serial
except ImportError:
    print("pyserial is required. Install it with 'pip install pyserial'.")
    sys.exit(1)

try:
    import matplotlib.pyplot as plt
    import pandas as pd
except ImportError:
    plt = None
    pd = None


def log_data(port, baud, output):
    """Log serial data to a CSV file with timestamps."""
    with serial.Serial(port, baud, timeout=1) as ser, open(output, 'a', newline='') as f:
        print(f"Logging started, writing to {output}. Stop the script to end logging.")
        try:
            while True:
                line = ser.readline().decode(errors='ignore').strip()
                if not line:
                    continue
                data = line.split(',')
                timestamp = datetime.datetime.now().isoformat()
                csv.writer(f).writerow([timestamp] + data)
        except KeyboardInterrupt:
            print("Logging stopped.")


def plot_csv(filename, column):
    """Plot a column from the CSV file using matplotlib."""
    if plt is None or pd is None:
        print("Matplotlib and pandas are required for plotting.")
        return
    df = pd.read_csv(filename)
    if column not in df.columns:
        print(f"Column '{column}' not found. Available columns: {list(df.columns)}")
        return
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    plt.figure()
    plt.plot(df['timestamp'], df[column])
    plt.xlabel('Time')
    plt.ylabel(column)
    plt.title(f'{column} vs Time')
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Serial Data Logger')
    parser.add_argument('--port', required=True, help='Serial port (e.g., COM3 or /dev/ttyUSB0)')
    parser.add_argument('--baud', type=int, default=9600, help='Baud rate (default: 9600)')
    parser.add_argument('--output', default='readings.csv', help='Output CSV file name')
    parser.add_argument('--plot-column', dest='plot_column', help='Column name to plot after logging')
    args = parser.parse_args()

    log_data(args.port, args.baud, args.output)
    if args.plot_column:
        plot_csv(args.output, args.plot_column)


if __name__ == '__main__':
    main()
