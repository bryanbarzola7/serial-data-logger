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
