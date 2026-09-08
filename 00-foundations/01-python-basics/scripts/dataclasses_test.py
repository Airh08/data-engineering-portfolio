from dataclasses import dataclass
import uuid

unique_id = str(uuid.uuid4())

@dataclass
class Order:
    order_id: str = "ORD001"
    customer_id: int = unique_id
    order_date: str = "2024-01-01"
    quantity: int = 1
    unit_price: float = 10.0
    status: str = "Pending"
    
@dataclass
class Customer:
    customer_id: int = unique_id
    name: str = "John Doe"
    email: str = "john.doe@example.com"


if __name__ == '__main__':
    order = Order(order_id="ORD001", customer_id=123)
    customer = Customer(customer_id=123, name="John Doe", email="john.doe@example.com")
    print(order)
    print(customer)