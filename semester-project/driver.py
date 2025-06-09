import sys
import json
from parse_temps import parse_raw_temps

def main():
    input_data = sys.argv[1]
    parsed_data = dict()
    with open(input_data, "r") as data_file:
        for data in parse_raw_temps(data_file):
            time, core_temps = data
            parsed_data[time] = core_temps

    output_file = "parsed_temps.json"
    with open(output_file, "w") as file:
        json.dump(parsed_data, file, indent=2, default=str)
    print(f"Parsed data saved to {output_file}")

if __name__ == "__main__":
    main()