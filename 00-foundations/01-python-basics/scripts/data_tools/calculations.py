from collections.abc import Iterable

from .formatters import format_currency


def calculate_total(prices: Iterable[float], tax_rate: float = 0.0) -> float:
    """Return the total of prices after applying a tax rate."""
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)


def summarize_total(total: float) -> str:
    """Return a formatted summary for a calculated total."""
    return f"Order total: {format_currency(total)}"