from collections import Counter
from dataclasses import dataclass
from enum import Enum, auto
from typing import Iterable


class OrderStatus(Enum):
    """
    Order Status
    """

    PENDING = auto()
    ACTIVE = auto()
    CONFIRMED = auto()


@dataclass(frozen=True)
class Item:
    """
    Item in the inventory and the order
    """

    name: str
    price: float | int


class Inventory:
    """
    Inventory for items
    """

    def __init__(self):
        self._stock = Counter()

    def add_stock(self, item: Item):
        self._stock[item] += 1

    def check_stock(self, item: Item, quantity: int) -> bool:
        return self._stock.get(item, 0) >= quantity

    def reduce_stock(self, item: Item, quantity: int) -> bool:
        if self.check_stock(item, quantity):
            self._stock[item] -= quantity
            return True
        return False


class Order:
    """
    Client order
    """

    def __init__(self):
        self.items = Counter()
        self.status = OrderStatus.PENDING

    def add_item(self, item: Item, quantity: int):
        self.items[item] += quantity
        self.status = OrderStatus.ACTIVE

    def calculate_total(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def confirm_order(self):
        self.status = OrderStatus.CONFIRMED


class OrderFacade:
    """
    Order Facade hides the logic of checking stock, reserving items, and calculating the total from the client
    """

    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def place_order(self, items: Iterable[Item], quantity: int):
        order = Order()
        for item in items:
            # 1. Check Inventory
            if not self.inventory.check_stock(item, quantity):
                raise ValueError(f"Items {item} not in inventory")

            # 2. Reduce Stock
            self.inventory.reduce_stock(item, quantity)

            # 3. Process order
            order.add_item(item, quantity)
            order.confirm_order()
        return order
