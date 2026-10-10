def merge_stock(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """Adds the quantities of two stock dicts. Items in only one dict keep their quantity. 
    The result is sorted by item name. Don't modify a or b."""
    merged = a.copy()
    for item, quantity in b.items():
        if item in merged:
            merged[item] += quantity
        else:
            merged[item] = quantity
    return dict(sorted(merged.items()))

def low_stock(stock: dict[str, int], limit: int) -> list[str]:
    """Returns the names of items with quantity below limit, sorted alphabetically."""
    low_items = [item for item, quantity in stock.items() if quantity < limit]
    return sorted(low_items)