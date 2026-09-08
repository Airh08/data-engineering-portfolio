from typing import Any, Literal


# Basic variable annotations
test_str: str = "This is a string"
test_int: int = 10
test_float: float = 10.5
test_list: list[int] = [1, 2, 3]
test_dict: dict[int, str] = {1: "first", 2: "second", 3: "third"}
test_tuple: tuple[int, str] = (1, "first")
test_set: set[str] = {"python", "typing"}
optional_name: str | None = None

# Type aliases make complex types easier to read and reuse.
OrderId = str
CustomerId = int
OrderStatus = Literal["pending", "paid", "cancelled"]
Order = dict[str, str | int | float]
Orders = list[Order]


orders: Orders = [
    {"id": "ORD-001", "customer_id": 42, "total": 125.50},
    {"id": "ORD-002", "customer_id": 84, "total": 80.00},
]


def test_function(test_param: str) -> str:
    """Return a string using a typed parameter and return value."""
    return test_param


def get_order_total(order: Order) -> float:
    """Read a numeric value from a nested order structure."""
    return float(order["total"])


def create_order(order_id: OrderId, customer_id: CustomerId, status: OrderStatus) -> Order:
    """Create an order using aliases and a restricted status value."""
    return {"id": order_id, "customer_id": customer_id, "status": status}


def find_order(orders: Orders, order_id: OrderId) -> Order | None:
    """Return the matching order or None when it does not exist."""
    return next((order for order in orders if order["id"] == order_id), None)


def describe_metadata(metadata: dict[str, Any]) -> str:
    """Accept metadata whose values can intentionally have different types."""
    return f"{metadata['source']}: {metadata['records']} records"


if __name__ == "__main__":
    result = test_function("Hello, World!")
    print(result)
    print(f"Tuple: {test_tuple}")
    print(f"Set: {test_set}")
    print(f"Optional value: {optional_name}")
    print(f"First order total: {get_order_total(orders[0])}")
    print(f"Created order: {create_order('ORD-003', 21, 'pending')}")
    print(f"Found order: {find_order(orders, 'ORD-002')}")
    print(describe_metadata({"source": "api", "records": 2, "valid": True}))