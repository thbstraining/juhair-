import json

def save_data_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
