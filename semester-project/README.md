# Course Project
This project processes core temperature logs to generate a readable report for each CPU core. It performs **piecewise linear interpolation** as well as **global least-squares approximation** on the collected data.

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