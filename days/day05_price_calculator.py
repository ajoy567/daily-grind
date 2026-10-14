
def final_price(price: float, discount_pct: float = 0, tax_pct: float = 18) -> float:
    """Return the price after applying a discount, then tax on the discounted amount.

    Order of operations: discount first, then tax on the reduced price.

    Args:
        price: Original price. Must be non-negative.
        discount_pct: Discount percentage in the range 0-100.
        tax_pct: Tax percentage applied to the discounted price. Defaults to 18.

    Returns:
        Final price rounded to 2 decimal places.

    Raises:
        ValueError: If price or tax_pct is negative, or discount_pct is outside 0-100.
    """
    if price < 0:
        raise ValueError("Price must be a non-negative value.")
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    if tax_pct < 0:
        raise ValueError("Tax percentage must be a non-negative value.")
    
    discounted_price = price - (price * discount_pct / 100)
    total = discounted_price + (discounted_price * tax_pct / 100)
    
    return round(total, 2)

def cart_total(*items: tuple[float, int]) -> float:
    """Return the total cost of a cart.

    No tax or discount is applied here — each pair is summed at face value.

    Args:
        *items: Any number of (price, qty) pairs.

    Returns:
        Total cost rounded to 2 decimal places. Returns 0.0 for an empty cart.
    """
    total = 0.0
    for price, qty in items:
        if price < 0 or qty <= 0:
            raise ValueError("Price must be a non-negative value and quantity must be a positive integer.")
        
        total += price * qty
    return round(total, 2)


def normalize(values: list[float]) -> list[float]:
    """Return a new list with values scaled to the 0-1 range (min-max scaling).

    The smallest input maps to 0.0 and the largest maps to 1.0. If all
    values are equal, returns a list of 0.0s (the range is undefined, so
    every point is treated as being at the start of the range). If the
    input is empty, returns an empty list.

    Does not modify the input list.

    Args:
        values: List of numbers to normalize.

    Returns:
        A new list of floats in the range [0.0, 1.0], the same length as
        the input.
    """
    if not values:
        return []
    
    min_val = min(values)
    max_val = max(values)
    data_range = max_val - min_val
    
    if data_range == 0:
        return [0.0 for _ in values]  # All values are the same, return a list of zeros.
    
    return [(value - min_val) / data_range for value in values]
