"""Inventory management system used to demonstrate static code analysis tools."""

import json
import logging
from datetime import datetime


def add_item(item="default", qty=0, logs=None, stock_data=None):
    """Add a quantity of an item to the inventory."""
    if logs is None:
        logs = []
    if stock_data is None:
        stock_data = {}
    if not isinstance(qty, int):
        logging.warning("Invalid quantity '%s' for item '%s'", qty, item)
        return stock_data
    if not isinstance(item, str):
        item = str(item)
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return stock_data


def remove_item(item, qty, stock_data):
    """Remove a quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning("Item '%s' not found in stock.", item)
    except ValueError as error:
        logging.error("Invalid quantity: %s", error)


def get_qty(item, stock_data):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("File not found. Starting with empty inventory.")
        return {}
    except json.JSONDecodeError:
        logging.error("Error decoding JSON. Returning empty inventory.")
        return {}


def save_data(stock_data, file="inventory.json"):
    """Save stock data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data(stock_data):
    """Print all inventory items."""
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")


def check_low_items(stock_data, threshold=5):
    """Return a list of items below the given threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main program execution."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    stock_data = {}
    stock_data = add_item("apple", 10, stock_data=stock_data)
    stock_data = add_item("banana", -2, stock_data=stock_data)
    stock_data = add_item("grape", 15, stock_data=stock_data)
    remove_item("apple", 3, stock_data)
    remove_item("orange", 1, stock_data)
    print("Apple stock:", get_qty("apple", stock_data))
    print("Low items:", check_low_items(stock_data))
    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)


if __name__ == "__main__":
    main()
