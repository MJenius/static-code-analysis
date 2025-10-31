import json
import logging
from datetime import datetime

stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add quantity of an item to inventory."""
    if logs is None:
        logs = []
    if not isinstance(qty, int):
        logging.warning(f"Invalid quantity '{qty}' for item '{item}'")
        return
    if not isinstance(item, str):
        item = str(item)
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """Remove quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning(f"Item '{item}' not found in stock.")
    except Exception as e:
        logging.error(f"Error removing item: {e}")

def get_qty(item):
    """Return quantity of a specific item."""
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Load stock data from JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning("File not found. Starting with empty inventory.")

def save_data(file="inventory.json"):
    """Save stock data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)

def print_data():
    """Print all inventory items."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")

def check_low_items(threshold=5):
    """Return items below threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]

def main():
    """Main program execution."""
    logging.basicConfig(level=logging.INFO)
    add_item("apple", 10)
    add_item("banana", -2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
