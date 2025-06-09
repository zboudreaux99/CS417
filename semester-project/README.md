# Course Project
This script reads a raw core temperature log file, parses the data using a provided `parse_temps` file, and writes the parsed output to a JSON file.

## Features
- Included test core data in `cpu_data/`
- Parses core temperature readings from a raw input file
- Outputs a structured JSON file with timestamps and corresponding core temperatures
- Command-line interface

## Usage
```bash
python driver.py cpu_data/sensors-2018.12.26.txt
```