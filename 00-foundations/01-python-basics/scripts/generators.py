def show_iterable_and_iterator() -> None:
    """Use iter to create an iterator from an iterable and consume it with next."""
    records = ["ORD-001", "ORD-002", "ORD-003"]
    records_iterator = iter(records)

    print(f"Iterable type: {type(records).__name__}")
    print(f"Iterator type: {type(records_iterator).__name__}")
    print(f"First record with next: {next(records_iterator)}")
    print(f"Second record with next: {next(records_iterator)}")


def consume_iterator(iterator: object) -> None:
    """Consume an iterator one value at a time until StopIteration."""
    while True:
        try:
            value = next(iterator)  # type: ignore[arg-type]
        except StopIteration:
            break
        print(f"Next value: {value}")


def order_records(records: list[dict[str, object]]):
    """Yield one record at a time instead of returning a complete list."""
    for record in records:
        print(f"Preparing record: {record['id']}")
        yield record


def show_generator_function() -> None:
    """Demonstrate that a generator function runs only when values are requested."""
    records = [
        {"id": "ORD-001", "status": "paid"},
        {"id": "ORD-002", "status": "pending"},
    ]
    generated_records = order_records(records)

    print(f"Generator function type: {type(generated_records).__name__}")
    print("Requesting the first generated record:")
    print(f"Generated: {next(generated_records)}")
    print("Requesting the remaining records:")
    consume_iterator(generated_records)


def show_generator_expression() -> None:
    """Create a generator expression and evaluate it value by value."""
    numbers = (number * number for number in range(1, 4))
    print(f"Generator expression type: {type(numbers).__name__}")
    print(f"First lazy result: {next(numbers)}")
    print(f"Remaining lazy results: {list(numbers)}")


def process_records_one_by_one(records: list[dict[str, object]]) -> int:
    """Process each record incrementally and return the number processed."""
    processed_count = 0
    for record in order_records(records):
        print(f"Processed record: {record['id']} ({record['status']})")
        processed_count += 1
    return processed_count


def main() -> None:
    """Run examples for iterables, iterators, and lazy generators."""
    show_iterable_and_iterator()
    print("Consuming a fresh iterator:")
    consume_iterator(iter([1, 2, 3]))
    show_generator_function()
    show_generator_expression()

    records = [
        {"id": "ORD-004", "status": "paid"},
        {"id": "ORD-005", "status": "pending"},
    ]
    print(f"Records processed: {process_records_one_by_one(records)}")


if __name__ == "__main__":
    main()