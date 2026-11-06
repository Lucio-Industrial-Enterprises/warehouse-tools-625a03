"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a nonnegative pick-list quantity."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be nonnegative")
    return quantity
