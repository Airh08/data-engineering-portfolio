def test_list_comprehension():
    # Example of list comprehension in python
    test_list = [x for x in range(10)]
    print(test_list)

def list_comprehension_with_condition():
    # Example of list comprehension with condition in python
    test_list = [x for x in range(10) if x % 2 == 0]
    print(test_list)

def list_comprehension_with_nested_loops():
    # Example of list comprehension with nested loops in python
    test_list = [x*y for x in range(3) for y in range(3)]
    print(test_list)

def list_comprehension_with_transformation():
    # Example of list comprehension with transformation in python
    test_list = [x**2 for x in range(10)]
    print(test_list)

def list_comprehension_dictionary():
    # Example of dictionary comprehension in python
    test_dict = {x: x**2 for x in range(10)}
    print(test_dict)

def list_comprehension_set():
    # Example of set comprehension in python
    test_set = {x for x in range(10)}
    print(test_set)

def list_comprehension_generator():
    # Example of generator comprehension in python
    test_gen = (x for x in range(10))
    print(test_gen)
    for x in test_gen:
        print(x)

if __name__ == '__main__':
    test_list_comprehension()
    list_comprehension_with_condition()
    list_comprehension_with_nested_loops()
    list_comprehension_with_transformation()
    list_comprehension_dictionary()
    list_comprehension_set()
    list_comprehension_generator()