# main.py
from products import PRODUCTS
from cart import ShoppingCart

def main():
    cart = ShoppingCart()
    while True:
        print("\n=== Shopping Menu ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. Update Cart Item Quantity")
        print("5. View Cart")
        print("6. Checkout & Exit")
        choice = input("Choose option: ")

        if choice == "1":
            # Show available products
            for pid, info in PRODUCTS.items():
                print(f"{pid}. {info['name']} - ₹{info['price']}")

        elif choice == "2":
            # Add item
            try:
                pid = int(input("Enter product id: "))
                qty = int(input("Quantity: "))
                if pid in PRODUCTS and qty > 0:
                    cart.add_item(pid, qty)
                else:
                    print("Invalid product id or quantity.")
            except ValueError:
                print("Enter numbers only.")

        elif choice == "3":
            # Remove item
            try:
                pid = int(input("Enter product id to remove: "))
                cart.remove_item(pid)
            except ValueError:
                print("Enter a valid number.")

        elif choice == "4":
            # Update quantity
            try:
                pid = int(input("Enter product id to update: "))
                if pid not in cart.items:
                    print("Item not in cart.")
                    continue
                qty = int(input("New quantity (0 to remove): "))
                cart.update_item(pid, qty)
            except ValueError:
                print("Enter valid numbers.")

        elif choice == "5":
            cart.view_cart(PRODUCTS)

        elif choice == "6":
            cart.view_cart(PRODUCTS)
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
