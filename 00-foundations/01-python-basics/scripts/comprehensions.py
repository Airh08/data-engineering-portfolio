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

def generator_expression():
    # A generator expression calculates values lazily.
    test_gen = (x for x in range(10))
    print(test_gen)
    for x in test_gen:
        print(x)


def list_comprehension_with_if_else():
    # The conditional expression goes before the for clause.
    labels = ["even" if number % 2 == 0 else "odd" for number in range(6)]
    print(labels)


def real_data_comprehension():
    orders = [
        {"id": "ORD-001", "customer": "Ana", "total": 125.50, "paid": True},
        {"id": "ORD-002", "customer": "Luis", "total": 80.00, "paid": False},
        {"id": "ORD-003", "customer": "Marta", "total": 210.00, "paid": True},
    ]
    paid_order_ids = [order["id"] for order in orders if order["paid"]]
    order_summaries = [
        f"{order['id']} - {order['customer']}: ${order['total']:.2f}"
        for order in orders
    ]
    print(paid_order_ids)
    print(order_summaries)


def nested_dictionary_comprehension():
    sales_by_month = {
        "January": {"online": 1200, "store": 800},
        "February": {"online": 1500, "store": 950},
    }
    monthly_totals = {
        month: sum(channel_sales.values())
        for month, channel_sales in sales_by_month.items()
    }
    print(monthly_totals)


def dictionary_items_example():
    prices = {"coffee": 3.50, "tea": 2.75, "cake": 4.00}
    discounted_prices = {
        item: round(price * 0.9, 2)
        for item, price in prices.items()
    }
    print(discounted_prices)


def compare_list_and_generator():
    numbers = range(1_000_000)
    numbers_as_list = [number * 2 for number in numbers]
    numbers_as_generator = (number * 2 for number in numbers)
    print(f"List type: {type(numbers_as_list).__name__}")
    print(f"Generator type: {type(numbers_as_generator).__name__}")
    print(f"First generator values: {[next(numbers_as_generator) for _ in range(3)]}")


def readable_loop():
    orders = [
        {"id": "ORD-001", "total": 125.50, "paid": True},
        {"id": "ORD-002", "total": 80.00, "paid": False},
        {"id": "ORD-003", "total": 210.00, "paid": True},
    ]
    paid_large_orders = []
    for order in orders:
        if order["paid"] and order["total"] > 100:
            paid_large_orders.append(f"{order['id']}: review shipment")
    print(paid_large_orders)


if __name__ == '__main__':
    test_list_comprehension()
    list_comprehension_with_condition()
    list_comprehension_with_nested_loops()
    list_comprehension_with_transformation()
    list_comprehension_dictionary()
    list_comprehension_set()
    generator_expression()
    list_comprehension_with_if_else()
    real_data_comprehension()
    nested_dictionary_comprehension()
    dictionary_items_example()
    compare_list_and_generator()
    readable_loop()