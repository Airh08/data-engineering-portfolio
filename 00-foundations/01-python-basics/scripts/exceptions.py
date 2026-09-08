import json
from pathlib import Path


def test_exception():
    # Example of exception handling in python
    test_list = [1, 2, 3]
    try:
        print(test_list[5])
    except IndexError as error:
        print(f"IndexError recuperable: {error}")
    else:
        print("La posición existe")
    finally:
        print("La operación terminó")
        
def test_exception_with_finally():
    # Example of exception handling with finally in python
    test_list = [1, 2, 3]
    try:
        print(test_list[5])
    except IndexError as error:
        print(f"IndexError recuperable: {error}")
    finally:
        print("This will always be executed")


class InvalidOrderError(Exception):
    """Raised when an order fails business validation."""


def validate_order(order: dict[str, object]) -> None:
    """Validate an order and raise specific errors for invalid input."""
    if "total" not in order:
        raise KeyError("La orden debe incluir 'total'")
    if not isinstance(order["total"], (int, float)):
        raise TypeError("'total' debe ser un número")
    if order["total"] <= 0:
        raise ValueError("'total' debe ser mayor que cero")


def parse_order(raw_order: str) -> dict[str, object]:
    """Parse JSON and convert malformed orders into a domain exception."""
    try:
        order = json.loads(raw_order)
    except json.JSONDecodeError as error:
        raise InvalidOrderError("La orden no contiene JSON válido") from error

    if not isinstance(order, dict):
        raise InvalidOrderError("La orden debe ser un objeto JSON")
    try:
        validate_order(order)
    except (KeyError, TypeError, ValueError) as error:
        raise InvalidOrderError("La orden no supera la validación") from error
    return order


def read_text_file(file_path: Path) -> str:
    """Read a text file and let FileNotFoundError reach the caller."""
    return file_path.read_text(encoding="utf-8")


def demonstrate_validation_errors() -> None:
    """Show specific recoverable validation errors without hiding defects."""
    invalid_orders: list[dict[str, object]] = [
        {},
        {"total": "free"},
        {"total": 0},
    ]
    for order in invalid_orders:
        try:
            validate_order(order)
        except KeyError as error:
            print(f"KeyError recuperable: {error}")
        except TypeError as error:
            print(f"TypeError recuperable: {error}")
        except ValueError as error:
            print(f"ValueError recuperable: {error}")


def main() -> None:
    """Run focused examples of recoverable and domain-specific exceptions."""
    test_exception()
    demonstrate_validation_errors()

    try:
        valid_order = parse_order('{"id": "ORD-001", "total": 125.50}')
        print(f"Orden válida: {valid_order}")
    except InvalidOrderError as error:
        print(f"InvalidOrderError: {error}")

    try:
        parse_order("not-json")
    except InvalidOrderError as error:
        print(f"InvalidOrderError: {error}")
        print(f"Causa original: {error.__cause__}")

    try:
        read_text_file(Path("missing-file.txt"))
    except FileNotFoundError as error:
        print(f"FileNotFoundError recuperable: {error.filename}")


if __name__ == "__main__":
    main()

if __name__ == '__main__':
    test_exception()
    test_exception_with_finally()