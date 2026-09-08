def test_exception():
    # Example of exception handling in python
    try:
        test_list = [1, 2, 3]
        print(test_list[5])
    except IndexError as e:
        print(f"IndexError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
        
def test_exception_with_finally():
    # Example of exception handling with finally in python
    try:
        test_list = [1, 2, 3]
        print(test_list[5])
    except IndexError as e:
        print(f"IndexError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("This will always be executed")

if __name__ == '__main__':
    test_exception()
    test_exception_with_finally()