def print_orders(order_list):
    for name, product, quantity in order_list:
        print(f"Customer: {name}, Product: {product}, Quantity: {quantity}")

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Alina", "Watches", 3),
    ("Karina", "Headphones", 4)
]

#usage
print_orders(orders)
