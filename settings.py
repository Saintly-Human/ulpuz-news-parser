import json
BASE_URL = 'https://upl.uz'

def safe_to_json(data, file_path):
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)