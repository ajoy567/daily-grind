
inventory = {
    "pen" : 50,
    "notebook" : 20,
    "stapler" : 3
}

def restock(inventory: dict[str, int], item: str, qty: int) -> None:
    """
    Add stock for an item, creating the item if it is new.

    Args:
        inventory (dict[str, int]): Item names mapped to quantities. Changed in place.
        item (str): Name of the item to restock.
        qty (int): Number of units to add. Must be above 0.

    Raises:
        ValueError: If qty is 0 or negative.
    """
    if qty <= 0:
        raise ValueError("Quantity must be above 0.")
    if item in inventory:
        inventory[item] += qty
    else:
        inventory[item] = qty
        
        
def sell(inventory: dict[str, int], item: str, qty: int) -> None:
    """
    Remove stock for an item. The item is deleted if its stock reaches 0.

    Args:
        inventory (dict[str, int]): Item names mapped to quantities. Changed in place.
        item (str): Name of the item to sell.
        qty (int): Number of units to sell. Must be above 0.

    Raises:
        ValueError: If qty is 0 or negative, if the item is not in the
            inventory, or if there is not enough stock.
    """
    if qty <= 0:
        raise ValueError("Quantity to sell must be a positive integer.")
    if item not in inventory:
        raise ValueError(f"{item} is not in inventory.")
    
    if inventory[item] < qty:
        raise ValueError(f"Not enough {item} in inventory to sell {qty} units.")
     
    inventory[item] -= qty
    if inventory[item] == 0:
        del inventory[item]
            
    
def low_stock(inventory: dict[str, int], threshold: int) -> list[str]:
    """
    Find items whose quantity is below a threshold.

    Args:
        inventory (dict[str, int]): Item names mapped to quantities.
        threshold (int): Items with a quantity strictly below this are included.

    Returns:
        list[str]: Names of the low-stock items. Empty if there are none.
    """
    return [item for item, qty in inventory.items() if qty < threshold]

    
def check_inventory(inventory: dict[str, int], item: str) -> int:
    """
    Get the current quantity of an item.

    Args:
        inventory (dict[str, int]): Item names mapped to quantities.
        item (str): Name of the item to look up.

    Returns:
        int: The quantity in stock, or 0 if the item is not in the inventory.
    """
    return inventory.get(item, 0)


restock(inventory, "pen", 10)
restock(inventory, "eraser", 5)
sell(inventory, "notebook", 5)
sell(inventory, "stapler", 99)
print(inventory)
print(low_stock(inventory, 10))