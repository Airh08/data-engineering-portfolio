# create varibale 
# variable_name = value

# Example variable type string
test_str = "Hello world"

# Example variable type int
test_int = 1

# Example variable type float
test_float = 100.56

# Example variable type list
test_list = ['apple','mango', 'grape']
test_list_empty = []

# Example variable type dict

test_dict = {1:'first', 2:'second', 3:'third'}
test_dict_empty = {}

# Example variable type tuple
test_tuple = (1, 2, 3)
twest_tuple_empty = ()

# Example variable type bool
test_bool = True

# Example variable type None
test_none = None

# Examples of mutable varaibles (list, dict) and immutable variables (str, int, float, tuple, bool, None)
vr_mutable = [1, 2, 3]
vr_immutable = 10

# Example of arithmetic operators
number_a = 10
number_b = 3
print(f"Arithmetic: addition={number_a + number_b}")
print(f"Arithmetic: subtraction={number_a - number_b}")
print(f"Arithmetic: multiplication={number_a * number_b}")
print(f"Arithmetic: division={number_a / number_b}")
print(f"Arithmetic: floor division={number_a // number_b}")
print(f"Arithmetic: remainder={number_a % number_b}")
print(f"Arithmetic: exponentiation={number_a ** number_b}")

# Example of comparison operators
print(f"Comparison: 10 == 3 -> {number_a == number_b}")
print(f"Comparison: 10 != 3 -> {number_a != number_b}")
print(f"Comparison: 10 > 3 -> {number_a > number_b}")
print(f"Comparison: 10 >= 3 -> {number_a >= number_b}")
print(f"Comparison: 10 < 3 -> {number_a < number_b}")
print(f"Comparison: 10 <= 3 -> {number_a <= number_b}")

# Example of logical operators
has_data = True
has_permission = False
print(f"Logical: has_data and has_permission -> {has_data and has_permission}")
print(f"Logical: has_data or has_permission -> {has_data or has_permission}")
print(f"Logical: not has_permission -> {not has_permission}")

# Example of assignment operators
total = 10
total += 5
total -= 2
total *= 2
total /= 2
total //= 3
total %= 4
total **= 2
print(f"Assignment operators result: {total}")

# is checks object identity; == checks value equality
first_numbers = [1, 2, 3]
second_numbers = [1, 2, 3]
same_numbers = first_numbers
print(f"is vs == (different objects): {first_numbers == second_numbers}, {first_numbers is second_numbers}")
print(f"is vs == (same object): {first_numbers == same_numbers}, {first_numbers is same_numbers}")

# isinstance() can validate more than one accepted type
raw_value = 42
if isinstance(raw_value, (int, float)):
    print("raw_value is an int or a float")

# Mutable objects can change through another reference; immutable values cannot.
original_rows = ["ready"]
rows_alias = original_rows
rows_alias.append("processed")
print(f"Mutable alias shares changes: {original_rows}")

original_status = "ready"
status_alias = original_status
status_alias += "-processed"
print(f"Immutable reassignment creates a new value: original={original_status}, alias={status_alias}")

# Example of conversion of variable types
test_str_to_int = int("10")
test_int_to_str = str(10)
test_float_to_int = int(100.56)
test_int_to_float = float(10)
test_str_to_float = float("100.56")
test_bool_to_str = str(True)

# print variable values
print(f"String: {test_str}")
print(f"Integer: {test_int}")
print(f"Float: {test_float}")
print(f"List: {test_list}")
print(f"Dictionary: {test_dict}")
print(f"Tuple: {test_tuple}")
print(f"Boolean: {test_bool}")
print(f"None: {test_none}")
print(f"Mutable variable: {vr_mutable}")
print(f"Immutable variable: {vr_immutable}")
print(f"String to Integer: {test_str_to_int}")
print(f"Integer to String: {test_int_to_str}")
print(f"Float to Integer: {test_float_to_int}")
print(f"Integer to Float: {test_int_to_float}")
print(f"String to Float: {test_str_to_float}")
print(f"Boolean to String: {test_bool_to_str}")

# Example of multiple assignment of variables
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Example of constants by convention (uppercase variable names)
PI = 3.14159
print(f"Constant PI: {PI}")

# Example of inspection of variable types
print(f"Type of test_str: {type(test_str)}")
print(f"Type of test_int: {type(test_int)}")
print(f"Type of test_float: {type(test_float)}")
print(f"Type of test_list: {type(test_list)}")
print(f"Type of test_dict: {type(test_dict)}")
print(f"Type of test_tuple: {type(test_tuple)}")
print(f"Type of test_bool: {type(test_bool)}")
print(f"Type of test_none: {type(test_none)}")

# Example of validation of variable types
if isinstance(test_str, str):
    print(f"test_str is of type str")
if isinstance(test_int, int):
    print(f"test_int is of type int")
if isinstance(test_float, float):
    print(f"test_float is of type float")
if isinstance(test_list, list):
    print(f"test_list is of type list")
if isinstance(test_dict, dict):
    print(f"test_dict is of type dict")
if isinstance(test_tuple, tuple):
    print(f"test_tuple is of type tuple")
if isinstance(test_bool, bool):
    print(f"test_bool is of type bool")
if isinstance(test_none, type(None)):
    print(f"test_none is of type NoneType")