"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total price.
"""

class Item:
    """
    Represents an item with a name and price.
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Initializes an item with a name and price.

        Args:
            name (str): Name of the item.
            price (float): Price of the item.
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Returns a string representation of the item.

        Returns:
            str: String in the format 'Item <name> costs <price>€'.
        """
        return f"Item {self.name} costs {self.price:.2f}€"
    
    def __repr__(self) -> str:
        """
        Returns a formal string representation of the item.

        Returns:
            str: String in the format '(name=<name>, price=<price>)'.
        """
        return f"(name={self.name}, price={self.price:.2f})"


class Shopping_Card:
    """
    Represents a shopping cart containing a list of items.
    """

    def __init__(self) -> None:
        """
        Initializes an empty shopping cart.
        """
        self.item_list: list[Item] = []

    def add_item(self, item: Item, amount: int = 1) -> None:
        """
        Adds a specified number of an item to the cart.

        Args:
            item (Item): The item to add.
            amount (int, optional): The number of items to add. Defaults to 1.
        """
        [self.item_list.append(item) for _ in range(amount)]

    def remove_item(self, item: Item, amount: int = 1) -> None:
        """
        Removes a specified number of an item from the cart.
        If the item doesn't exist or the amount exceeds the available quantity, 
        removes as many as possible.

        Args:
            item (Item): The item to remove.
            amount (int, optional): The number of items to remove. Defaults to 1.

        Prints:
            str: Feedback on how many items were removed or if the item was not found.
        """
        removed_count = 0

        # Iterate over a copy of the list to avoid modifying the list during iteration.
        for existing_item in self.item_list[:]:
            if existing_item.name == item.name:  # Match items by name.
                self.item_list.remove(existing_item)
                removed_count += 1
                if removed_count == amount:  # Stop once the required amount is removed.
                    break

        if removed_count > 0:
            print(f"Removed {removed_count} of {item.name}")
        else:
            print(f"{item.name} not found in inventory")

    def calc_total_price(self) -> float:
        """
        Calculates the total price of all items in the cart.

        Returns:
            float: Total price of items in the cart.
        """
        total_price = 0
        for item in self.item_list:
            total_price += item.price

        return total_price
    
    def list_card(self) -> None:
        """
        Prints the list of all items in the cart.
        """
        print(self.item_list)


# Example usage of the Shopping_Card class.
if __name__ == "__main__":
    # Create a shopping cart instance.
    card = Shopping_Card()

    # Add items to the cart.
    card.add_item(Item("Glue", 5))                  # Add one Glue item.
    card.add_item(Item("Rice", 10), amount=3)       # Add three Rice items.
    card.add_item(Item("Book", 16.5), amount=2)     # Add two Book items.
    card.add_item(Item("Laptop", 1200))             # Add one Laptop item.

    # List items in the cart and calculate the total price.
    card.list_card()
    print(f"Total price: {card.calc_total_price()}")

    # Remove items from the cart.
    card.remove_item(Item("Rice", 10), amount=3)

    # List items again and calculate the updated total price.
    card.list_card()
    print(f"Total price: {card.calc_total_price()}")
