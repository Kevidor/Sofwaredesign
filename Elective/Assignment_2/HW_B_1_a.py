"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total price.
"""
class Item():
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Item {self.name} costs {self.price:.2f}€"
    
    def __repr__(self) -> str:
        return f"(name={self.name}, price={self.price:.2f})"

class Shopping_Card():
    def __init__(self) -> None:
        self.item_list: list[Item] = []

    def add_item(self, item: Item, amount: int = 1) -> None:
        [self.item_list.append(item) for _ in range(amount)]

    def remove_item(self, item: Item, amount: int = 1) -> None:
        removed_count = 0

        for existing_item in self.item_list[:]:
            if existing_item.name == item.name:
                self.item_list.remove(existing_item)
                removed_count += 1
                if removed_count == amount:
                    break

        if removed_count > 0:
            print(f"Removed {removed_count} of {item.name}")
        else:
            print(f"{item.name} not found in inventory")


    def calc_total_price(self) -> float:
        total_price = 0
        for item in self.item_list:
            total_price += item.price

        return total_price
    
    def list_card(self) -> None:
        print(self.item_list)

card = Shopping_Card()
card.add_item(Item("Glue", 5))
card.add_item(Item("Rice", 10), amount= 3)
card.add_item(Item("Book", 16.5), amount= 2)
card.add_item(Item("Laptop", 1200))

card.list_card()
print(f"Total price: {card.calc_total_price()}")

card.remove_item(Item("Rice", 10), amount= 3)

card.list_card()
print(f"Total price: {card.calc_total_price()}")
