# varibales annotation
test_str: str = "This is a string"
test_int: int = 10
test_float: float = 10.5
test_list: list = [1, 2, 3]
test_dict: dict = {1: 'first', 2: 'second', 3: 'third'}

#function parameters and return type (-> is used to indicate the return type)
def test_function(test_param: str) -> str:
    return test_param

if __name__ == '__main__':
    result = test_function("Hello, World!")
    print(result)