from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import uuid


def generate_id(prefix: str) -> str:
    """Generate a readable identifier for a domain object."""
    return f"{prefix}-{uuid.uuid4()}"


@dataclass(frozen=True)
class Customer:
    """Immutable customer record."""

    customer_id: str = field(default_factory=lambda: generate_id("CUS"))
    name: str = "John Doe"
    email: str = field(
        default="john.doe@example.com",
        metadata={"description": "Primary customer email"},
    )
    phone: str | None = None

    def __post_init__(self) -> None:
        if "@" not in self.email:
            raise ValueError("Customer email must contain '@'")


@dataclass
class Order:
    """Order record with validation and a nested optional customer."""

    order_id: str = field(default_factory=lambda: generate_id("ORD"))
    customer_id: str = field(default_factory=lambda: generate_id("CUS"))
    order_date: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
        metadata={"description": "UTC order creation time"},
    )
    quantity: int = 1
    unit_price: float = 10.0
    status: str = "pending"
    customer: Customer | None = None
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("Order quantity must be greater than zero")
        if self.unit_price < 0:
            raise ValueError("Order unit price cannot be negative")
        if self.status not in {"pending", "paid", "cancelled"}:
            raise ValueError(f"Unsupported order status: {self.status}")

    @property
    def total(self) -> float:
        """Return the order total."""
        return self.quantity * self.unit_price


if __name__ == "__main__":
    customer = Customer(
        customer_id="CUS-001",
        name="John Doe",
        email="john.doe@example.com",
    )
    order = Order(
        order_id="ORD-001",
        customer_id=customer.customer_id,
        quantity=2,
        unit_price=25.0,
        status="paid",
        customer=customer,
        tags=["priority", "online"],
    )

    print(order)
    print(f"Order total: {order.total}")
    print(f"Nested customer: {order.customer}")
    print(f"As dictionary: {asdict(order)}")

    try:
        Order(quantity=0)
    except ValueError as error:
        print(f"Validation error: {error}")

    try:
        Customer(email="invalid-email")
    except ValueError as error:
        print(f"Customer validation error: {error}")