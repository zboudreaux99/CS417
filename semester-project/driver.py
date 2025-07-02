import sys
import json
from parse_temps import parse_raw_temps
from linear_interpolation import linear_interpolate, write_interpolation_files

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

    # Sort keys and align values
    sorted_items = sorted(parsed_data.items())
    x_vals = [t for t, _ in sorted_items]
    y_vals = [temps for _, temps in sorted_items]

    # Write interpolation equations per core
    base_name = input_data.replace(".txt", "")
    write_interpolation_files(x_vals, y_vals, base_filename=base_name)
    print(f"Interpolation files written with base name: {base_name}")

if __name__ == "__main__":
    main()