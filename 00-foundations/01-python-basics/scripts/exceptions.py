def test_exception():
    # Example of exception handling in python
    try:
        test_list = [1, 2, 3]
        print(test_list[5])
    except IndexError as e:
        print(f"IndexError: {e}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == '__main__':
    test_exception()