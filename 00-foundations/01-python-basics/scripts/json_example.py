import json
from pathlib import Path

def search_json_files(filename="info.json"):
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "src" / filename
    if not file_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")
    return file_path

def test_json():
    # Example of json in python
    test_dict = {1:'first', 2:'second', 3:'third'}
    test_json = json.dumps(test_dict)
    with open(search_json_files("example_dump.json"), 'w') as f:
        f.write(test_json)
    print(test_json)
    
def test_json_read():
    file_path = search_json_files()
    # Example of json read in python
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def test_json_loads():
    # Example of json loads in python
    test_dict = {1:'first', 2:'second', 3:'third'}
    test_json = json.dumps(test_dict)
    data = json.loads(test_json)
    return data

def test_nested_json():
    # Example of nested json in python
    test_dict = {1:'first', 2:'second', 3:'third', 'nested': {'a': 1, 'b': 2}}
    test_json = json.dumps(test_dict)
    data = json.loads(test_json)
    return data

if __name__ == '__main__':
    print("Testing json")
    test_json()
    print("Testing json read")
    data = test_json_read()
    print(data)
    print("Testing json loads")
    data = test_json_loads()
    print(data)
    print("Testing json anidado")
    data = test_nested_json()
    print(data)