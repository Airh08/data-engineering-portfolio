def classify_score(score: int) -> str:
    """Return a label using an if/elif/else decision tree."""
    if score >= 90:
        return "excellent"
    elif score >= 60:
        return "passing"
    else:
        return "needs improvement"


def show_for_loop(values: list[str]) -> None:
    """Print every value in a collection with a for loop."""
    for value in values:
        print(f"For loop value: {value}")


def show_while_loop(start: int) -> None:
    """Count down to zero with a while loop."""
    counter = start
    while counter > 0:
        print(f"While loop counter: {counter}")
        counter -= 1


def find_first_pending(statuses: list[str]) -> str | None:
    """Return the first pending status and stop searching with break."""
    first_pending = None
    for status in statuses:
        if status == "pending":
            first_pending = status
            break
    return first_pending


def show_continue(values: list[int]) -> None:
    """Skip odd values with continue and print only even values."""
    for value in values:
        if value % 2 != 0:
            continue
        print(f"Even value: {value}")


def show_range() -> None:
    """Use range to generate a sequence of numbers."""
    for number in range(1, 4):
        print(f"Range value: {number}")


def show_enumerate(values: list[str]) -> None:
    """Print each value together with its position using enumerate."""
    for position, value in enumerate(values, start=1):
        print(f"Item {position}: {value}")


def show_zip(names: list[str], roles: list[str]) -> None:
    """Combine two collections into pairs with zip."""
    for name, role in zip(names, roles):
        print(f"{name}: {role}")


def describe_command(command: str) -> str:
    """Return a message by matching a command with match/case."""
    match command:
        case "start":
            return "The process is starting"
        case "stop":
            return "The process is stopping"
        case _:
            return "Unknown command"


def main() -> None:
    """Run examples for Python control-flow statements."""
    print(f"Score result: {classify_score(85)}")
    show_for_loop(["extract", "transform", "load"])
    show_while_loop(3)
    statuses = ["paid", "pending", "failed"]
    print(f"First pending status: {find_first_pending(statuses)}")
    show_continue([1, 2, 3, 4])
    show_range()
    show_enumerate(["customers", "orders"])
    show_zip(["Ana", "Luis"], ["data engineer", "analyst"])
    print(f"Match result: {describe_command('start')}")


if __name__ == "__main__":
    main()