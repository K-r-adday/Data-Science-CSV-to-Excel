import pandas as pd
import sys

def convert_to_excel(input_file_path, output_excel_path, file_type='csv'):
    # Read the input file based on its type
    if file_type == 'csv':
        df = pd.read_csv(input_file_path, on_bad_lines='warn')
    elif file_type == 'txt':
        # Assuming the text file is delimited, e.g., comma-separated
        df = pd.read_csv(input_file_path, delimiter=',', on_bad_lines='warn')
    else:
        raise ValueError("Unsupported file type. Use 'csv' or 'txt'.")

    # Write the data to an Excel file
    df.to_excel(output_excel_path, index=False, engine='openpyxl')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 csvtoexl.py <input_file_path> <output_excel_path> <file_type>")
    else:
        input_file_path = sys.argv[1]
        output_excel_path = sys.argv[2]
        file_type = sys.argv[3]
        convert_to_excel(input_file_path, output_excel_path, file_type)
        print(f"Converted '{input_file_path}' to '{output_excel_path}'.")
