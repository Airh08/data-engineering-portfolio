import json
from pathlib import Path

def search_json_files():
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "src" / "info.json"
    if not file_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")
    return file_path

def test_json():
    # Example of json in python
    test_dict = {1:'first', 2:'second', 3:'third'}
    test_json = json.dumps(test_dict)
    print(test_json)
    
def test_json_read():
    file_path = search_json_files()
    # Example of json read in python
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    print("Testing json")
    test_json()
    print("Testing json read")
    data = test_json_read()
    print(data)