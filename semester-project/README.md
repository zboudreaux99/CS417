# Course Project
This script reads a raw core temperature log file, parses the data using a provided `parse_temps` module, and writes the parsed output to both a structured JSON file and a set of per-core linear interpolation files.

## Features
- Included test core data in `cpu_data/`
- Parses core temperature readings from a raw input file
- Outputs a structured JSON file with timestamps and corresponding core temperatures
- Performs piecewise linear interpolation for each CPU core between sampled time points
- Generates one text file per core with readable `y = b + mx` equations for each interval
- Command-line interface

## Usage
```bash
python driver.py cpu_data/sensors-2018.12.26.txt
```