# Example of basic function in python
def test_fun():
    print("This is a function")
    
def test_fun_with_args(arg1, arg2):
    print(f"This is a function with arguments: {arg1} and {arg2}")

def test_fun_with_return():
    return "This is a function with return value"

def test_fun_with_default_args(arg1="default1", arg2="default2"):
    print(f"This is a function with default arguments: {arg1} and {arg2}")

def test_fun_with_variable_args(*args):
    print(f"This is a function with variable arguments: {args}")

def test_fun_with_keyword_args(**kwargs):
    print(f"This is a function with keyword arguments: {kwargs}")

def test_fun_with_variable_and_keyword_args(*args, **kwargs):
    print(f"This is a function with variable arguments: {args} and keyword arguments: {kwargs}")

def test_fun_with_return_and_args(arg1, arg2):
    return f"This is a function with return value and arguments: {arg1} and {arg2}"

def calculate_sum(*args):
    return sum(args)

def calculate_product(*args):
    product = 1
    for num in args:
        product *= num
    return product

def calculate_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def calculate_max(*args):
    return max(args)

def calculate_min(*args):
    return min(args)

if __name__ == '__main__':
    test_fun()
    test_fun_with_args("Hello", "World")
    test_fun_with_default_args()
    result = test_fun_with_return()
    print(f"Function with return value: {result}")
    test_fun_with_variable_args(1, 2, 3, 4, 5)
    test_fun_with_keyword_args(arg1="value1", arg2="value2")
    test_fun_with_variable_and_keyword_args(1, 2, 3, arg3="value3", arg4="value4")
    sum_result = calculate_sum(1, 2, 3, 4, 5)
    print(f"Sum: {sum_result}")
    product_result = calculate_product(1, 2, 3, 4, 5)
    print(f"Product: {product_result}")
    average_result = calculate_average(1, 2, 3, 4, 5)
    print(f"Average: {average_result}")
    max_result = calculate_max(1, 2, 3, 4, 5)
    print(f"Max: {max_result}")
    min_result = calculate_min(1, 2, 3, 4, 5)
    print(f"Min: {min_result}")