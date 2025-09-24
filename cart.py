# cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product_id: quantity}

    def add_item(self, product_id, qty=1):
        """Add or increase quantity of an item."""
        self.items[product_id] = self.items.get(product_id, 0) + qty

    def remove_item(self, product_id):
        """Remove an item completely."""
        if product_id in self.items:
            del self.items[product_id]

    def update_item(self, product_id, qty):
        """
        Update the quantity of an item.
        If qty is 0 or negative, the item is removed.
        """
        if product_id in self.items:
            if qty > 0:
                self.items[product_id] = qty
            else:
                del self.items[product_id]

    def view_cart(self, catalog):
        """Display current items and total price."""
        if not self.items:
            print("Cart is empty.")
            return
        total = 0
        print("\n--- Your Cart ---")
        for pid, qty in self.items.items():
            name = catalog[pid]["name"]
            price = catalog[pid]["price"]
            line_total = price * qty
            total += line_total
            print(f"{name} x {qty} = ₹{line_total}")
        print(f"Total: ₹{total}\n")

