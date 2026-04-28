from abc import ABC, abstractmethod
from datetime import datetime

# ------------------ USER CLASS ------------------
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.cart = Cart()

    def add_to_cart(self, item, quantity):
        self.cart.add_item(item, quantity)

    def place_order(self):
        if not self.cart.items:
            print("Cart is empty!")
            return None
        order = Order(self, self.cart.items)
        self.cart.clear_cart()
        return order


# ------------------ MENU ITEM ------------------
class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


# ------------------ RESTAURANT ------------------
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

    def show_menu(self):
        for item in self.menu:
            print(f"{item.item_id} | {item.name} | ₹{item.price}")


# ------------------ CART ------------------
class Cart:
    def __init__(self):
        self.items = {}  # item: quantity

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"{item.name} added to cart.")

    def calculate_total(self):
        total = 0
        for item, qty in self.items.items():
            total += item.price * qty
        return total

    def clear_cart(self):
        self.items = {}


# ------------------ ORDER ------------------
class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items.copy()
        self.order_time = datetime.now()
        self.status = "Placed"
        self.total = self.calculate_total()

    def calculate_total(self):
        total = 0
        for item, qty in self.items.items():
            total += item.price * qty

        # Discount logic
        if total > 500:
            total *= 0.9  # 10% discount

        return total

    def update_status(self, status):
        self.status = status


# ------------------ PAYMENT (ABSTRACTION) ------------------
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


# ------------------ MAIN PROGRAM ------------------
def main():
    # Create restaurant
    restaurant = Restaurant("Food Hub")

    # Add menu items
    item1 = MenuItem(1, "Pizza", 250)
    item2 = MenuItem(2, "Burger", 150)
    item3 = MenuItem(3, "Pasta", 200)

    restaurant.add_item(item1)
    restaurant.add_item(item2)
    restaurant.add_item(item3)

    user = User("Kartiki", 101)

    while True:
        print("\n1. Show Menu\n2. Add to Cart\n3. Place Order\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            restaurant.show_menu()

        elif choice == "2":
            item_id = int(input("Enter item ID: "))
            qty = int(input("Enter quantity: "))

            for item in restaurant.menu:
                if item.item_id == item_id:
                    user.add_to_cart(item, qty)

        elif choice == "3":
            order = user.place_order()
            if order:
                print(f"Order placed! Total: ₹{order.total}")

                # Payment
                print("1. UPI\n2. Card")
                pay_choice = input("Select payment: ")

                if pay_choice == "1":
                    payment = UPI()
                else:
                    payment = Card()

                payment.pay(order.total)

                order.update_status("Delivered")
                print("Order Delivered!")

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()