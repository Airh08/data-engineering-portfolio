def show_collection_types() -> None:
    """Create and display the basic Python collection types."""
    names = ["Ana", "Luis", "Marta"]
    coordinates = (40.4, -3.7)
    customer = {"name": "Ana", "active": True}
    unique_tags = {"python", "data", "python"}

    print(f"List: {names}")
    print(f"Tuple: {coordinates}")
    print(f"Dictionary: {customer}")
    print(f"Set removes duplicates: {unique_tags}")


def show_indexing_and_slicing() -> None:
    """Access individual values and ranges from ordered collections."""
    stages = ["extract", "transform", "load", "monitor"]
    print(f"First item: {stages[0]}")
    print(f"Last item: {stages[-1]}")
    print(f"First two items: {stages[:2]}")
    print(f"Items from the second onward: {stages[1:]}")
    print(f"Every other item: {stages[::2]}")


def show_list_methods() -> None:
    """Modify a list with append, extend, pop, and remove."""
    tasks = ["extract"]
    tasks.append("transform")
    tasks.extend(["load", "monitor"])
    removed_last = tasks.pop()
    tasks.remove("transform")

    print(f"List after methods: {tasks}")
    print(f"Value returned by pop: {removed_last}")


def show_dictionary_methods() -> None:
    """Read dictionary data with get, keys, values, and items."""
    order = {"id": "ORD-001", "status": "paid", "total": 125.50}

    print(f"Existing value with get: {order.get('status')}")
    print(f"Missing value with default: {order.get('customer', 'unknown')}")
    print(f"Keys: {list(order.keys())}")
    print(f"Values: {list(order.values())}")
    print(f"Items: {list(order.items())}")


def show_set_operations() -> None:
    """Demonstrate common operations between sets."""
    python_students = {"Ana", "Luis", "Marta"}
    sql_students = {"Luis", "Marta", "Diego"}

    print(f"Union: {python_students | sql_students}")
    print(f"Intersection: {python_students & sql_students}")
    print(f"Only in Python: {python_students - sql_students}")
    print(f"Only in one course: {python_students ^ sql_students}")


def show_nested_structures() -> None:
    """Read values from a list of dictionaries containing nested data."""
    orders = [
        {
            "id": "ORD-001",
            "customer": {"name": "Ana", "city": "Madrid"},
            "items": ["coffee", "cake"],
        },
        {
            "id": "ORD-002",
            "customer": {"name": "Luis", "city": "Valencia"},
            "items": ["tea"],
        },
    ]

    first_order = orders[0]
    print(f"Nested customer name: {first_order['customer']['name']}")
    print(f"Nested first item: {first_order['items'][0]}")
    print(f"Nested order slice: {orders[:1]}")


def main() -> None:
    """Run examples for Python collections and collection operations."""
    show_collection_types()
    show_indexing_and_slicing()
    show_list_methods()
    show_dictionary_methods()
    show_set_operations()
    show_nested_structures()


if __name__ == "__main__":
    main()