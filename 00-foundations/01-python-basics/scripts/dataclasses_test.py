from dataclasses import dataclass

@dataclass
class TestDataClass:
    name: str
    age: int


if __name__ == '__main__':
    test_data = TestDataClass(name="John", age=30)
    print(test_data)