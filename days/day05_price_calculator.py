
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
        total += price * qty
    return round(total, 2)
