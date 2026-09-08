import pathlib

# Example of using pathlib in python
path = pathlib.Path('.') 

def test_pathlib():
    # Example of using pathlib in python
    print(path.resolve())
    print(path.exists())
    print(path.is_dir())
    print(path.is_file())
    
if __name__ == '__main__':
    test_pathlib()