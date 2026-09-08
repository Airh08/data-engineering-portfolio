def show_slicing(text: str) -> None:
    """Access portions of a string with slicing."""
    print(f"First three characters: {text[:3]}")
    print(f"Characters from position 4: {text[3:]}")
    print(f"Every second character: {text[::2]}")
    print(f"Reversed text: {text[::-1]}")


def normalize_text(value: str) -> str:
    """Remove surrounding whitespace and collapse internal whitespace."""
    return " ".join(value.strip().split())


def parse_order_line(raw_line: str) -> dict[str, str | float]:
    """Parse and normalize a comma-separated order into structured data."""
    fields = raw_line.split(",")
    if len(fields) != 3:
        raise ValueError("An order must contain id, customer, and amount")

    order_id = normalize_text(fields[0]).upper()
    customer = normalize_text(fields[1]).title()
    amount_text = normalize_text(fields[2]).replace("$", "")

    if not order_id.startswith("ORD-"):
        raise ValueError(f"Invalid order id: {order_id}")
    if not amount_text:
        raise ValueError("Order amount cannot be empty")

    return {
        "order_id": order_id,
        "customer": customer,
        "amount": float(amount_text),
    }


def demonstrate_string_methods() -> None:
    """Demonstrate common string methods used in data preparation."""
    raw_status = "  PAID  "
    normalized_status = raw_status.strip().lower()
    report_parts = ["order", "ready", normalized_status]
    report = " | ".join(report_parts)

    print(f"strip: '{raw_status.strip()}'")
    print(f"lower: {raw_status.lower()}")
    print(f"upper: {normalized_status.upper()}")
    print(f"replace: {report.replace('|', '->')}")
    print(f"startswith: {normalized_status.startswith('p')}")
    print(f"endswith: {normalized_status.endswith('id')}")
    print(f"find: {report.find('ready')}")
    print(f"join: {report}")


def format_order(order: dict[str, str | float]) -> str:
    """Create a readable output line with an f-string."""
    return f"{order['order_id']} | {order['customer']} | ${order['amount']:.2f}"


def main() -> None:
    """Run string operations and a complete parsing and normalization pipeline."""
    demonstrate_string_methods()
    show_slicing("DATA")

    raw_order = "  ORD-001, John Doe, 100.50  "
    order = parse_order_line(raw_order)
    print(f"Raw input: {raw_order!r}")
    print(f"Structured data: {order}")
    print(f"Formatted with f-string: {format_order(order)}")


if __name__ == "__main__":
    main()