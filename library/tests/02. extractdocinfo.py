import os
import pandas as pd
import json

def get_columns_from_file(filepath):
    try:
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath, nrows=1)
        elif filepath.endswith('.json'):
            df = pd.read_json(filepath, lines=True if filepath.endswith('.jsonl') else False)
        else:
            return []
        return list(df.columns)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def scan_folder_for_schema(folder_path):
    summary = {}
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv') or file.endswith('.json'):
                full_path = os.path.join(root, file)
                columns = get_columns_from_file(full_path)
                summary[file] = columns

    return summary

def save_summary_to_json(summary, output_path='summary_of_columns.json'):
    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=4)

# Example usage
if __name__ == "__main__":
    folder_to_scan = input("Enter the folder path to scan: ").strip()
    summary = scan_folder_for_schema(folder_to_scan)
    save_summary_to_json(summary)
    print(f"\nSummary saved to summary_of_columns.json\n")
