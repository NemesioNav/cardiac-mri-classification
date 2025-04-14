import os
import pandas as pd

def parse_case_file(filepath):
    with open(filepath, 'r', encoding='latin1') as f:
        lines = f.readlines()

    data = {}

    # Get label from first line
    if not lines:
        raise ValueError(f"The file {filepath} is empty and cannot be processed.")
    label_line = lines[0].strip()
    if label_line.startswith('Case N'):
        data['label'] = 'normal'
    elif label_line.startswith('Case P'):
        data['label'] = 'pathological'
    else:
        raise ValueError(f"Unexpected case label '{label_line}' in file {filepath}")

    # Extract key-value pairs
    for line in lines[1:]:
        if ':' not in line:
            continue
        key, value = line.strip().split(':', 1)
        key = key.strip().replace('�', '').replace(' ', '_')
        value = value.strip()
        data[key] = value

    return data

def build_dataframe_from_txts(folder_path):
    rows = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            full_path = os.path.join(folder_path, filename)
            case_data = parse_case_file(full_path)
            rows.append(case_data)

    df = pd.DataFrame(rows)
    return df