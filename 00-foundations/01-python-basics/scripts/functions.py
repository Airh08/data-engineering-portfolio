from collections.abc import Callable


def test_fun() -> None:
    """Print a simple message to demonstrate a basic function."""
    print("This is a function")
    
def test_fun_with_args(arg1: str, arg2: str) -> None:
    """Print two given arguments as part of a simple example."""
    print(f"This is a function with arguments: {arg1} and {arg2}")

def test_fun_with_return() -> str:
    """Return a sample string to demonstrate a function with a return value."""
    return "This is a function with return value"

def test_fun_with_default_args(arg1: str = "default1", arg2: str = "default2") -> None:
    """Print two arguments, using default values when none are provided."""
    print(f"This is a function with default arguments: {arg1} and {arg2}")

def test_fun_with_variable_args(*args: int) -> None:
    """Print all positional arguments passed to the function."""
    print(f"This is a function with variable arguments: {args}")

def test_fun_with_keyword_args(**kwargs: str) -> None:
    """Print all keyword arguments passed to the function."""
    print(f"This is a function with keyword arguments: {kwargs}")

def test_fun_with_variable_and_keyword_args(*args: int, **kwargs: str) -> None:
    """Print positional and keyword arguments together in one example."""
    print(f"This is a function with variable arguments: {args} and keyword arguments: {kwargs}")

def test_fun_with_return_and_args(arg1: str, arg2: str) -> str:
    """Return a formatted message using two provided arguments."""
    return f"This is a function with return value and arguments: {arg1} and {arg2}"

def calculate_sum(*args: float) -> float:
    """Return the sum of all numeric arguments passed to the function."""
    return sum(args)

def calculate_product(*args: float) -> float:
    """Return the product of all numeric arguments passed to the function."""
    product = 1
    for num in args:
        product *= num
    return product

def calculate_average(*args: float) -> float:
    """Return the arithmetic average of the given numbers; returns 0 for an empty input."""
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def calculate_max(*args: float) -> float:
    """Return the largest value among the arguments."""
    return max(args)

def calculate_min(*args: float) -> float:
    """Return the smallest value among the arguments."""
    return min(args)


def calculate_average_with_options(*, total: float, count: int) -> float:
    """Calculate an average using required keyword-only arguments."""
    if count == 0:
        return 0
    return total / count


def divide_numbers(dividend: float, /, divisor: float) -> float:
    """Use a positional-only dividend and a regular divisor."""
    return dividend / divisor


def square(number: int) -> int:
    """Return the square of a number."""
    return number * number


def add_tax(price: float, tax_rate: float) -> float:
    """Return a price after applying a tax rate."""
    return price * (1 + tax_rate)


def transform_numbers(
    numbers: list[int], transform: Callable[[int], int]
) -> list[int]:
    """Apply a function to every number and return the transformed list."""
    return list(map(transform, numbers))


def select_numbers(numbers: list[int], condition: Callable[[int], bool]) -> list[int]:
    """Return only numbers that satisfy the given condition."""
    return list(filter(condition, numbers))


def sort_people_by_age(people: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    """Return people ordered by the value stored in their ``age`` key."""
    return sorted(people, key=lambda person: person["age"])


def describe_result(label: str, value: object) -> str:
    """Build presentation text without printing from the business logic."""
    return f"{label}: {value}"


def main() -> None:
    """Run examples and keep presentation decisions in the caller."""
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

    print(f"Keyword-only average: {calculate_average_with_options(total=15, count=5)}")
    print(f"Positional-only example: {divide_numbers(10, 2)}")
    print(f"Lambda: {transform_numbers([1, 2, 3], lambda number: number * 10)}")
    print(f"Map with named function: {transform_numbers([1, 2, 3], square)}")
    print(f"Filter: {select_numbers([1, 2, 3, 4, 5], lambda number: number % 2 == 0)}")

    people = [
        {"name": "Ana", "age": 32},
        {"name": "Luis", "age": 25},
    ]
    print(f"Sorted by age: {sort_people_by_age(people)}")
    print(describe_result("Price with tax", add_tax(100, 0.21)))


if __name__ == "__main__":
    main()