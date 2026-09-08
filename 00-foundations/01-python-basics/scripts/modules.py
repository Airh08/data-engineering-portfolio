import math
from statistics import mean

from data_tools import calculate_total, summarize_total


def main() -> None:
    """Run import examples from this script, not from the reusable package."""
    print(f"Square root: {math.sqrt(16)}")
    print(f"Mean: {mean([10, 20, 30])}")
    prices = [12.50, 8.00, 20.00]
    total = calculate_total(prices, tax_rate=0.21)
    print(summarize_total(total))


if __name__ == "__main__":
    main()