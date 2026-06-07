import itertools

import pytest

from design_patterns.structural.facade import (Inventory, Item, Order,
                                               OrderFacade, OrderStatus)


@pytest.fixture(scope="class")
def cup_of_coffee() -> tuple[Item, Item, Item]:
    """
    A cup of coffee
    """
    return Item("Cup", 2), Item("Spoon", 0.5), Item("Coffee", 5)


@pytest.fixture(scope="function")
def inventory(cup_of_coffee) -> Inventory:
    """
    Inventory with 5 coffee cups
    """
    inventory = Inventory()
    for iteration in itertools.repeat(cup_of_coffee, 5):
        for item in iteration:
            inventory.add_stock(item)
    return inventory


@pytest.fixture(scope="function")
def order_facade(inventory: Inventory) -> OrderFacade:
    """
    OrderFacade instance
    """
    return OrderFacade(inventory)


def test_place_order_without_facade(inventory: Inventory, cup_of_coffee: tuple[Item, Item, Item]):
    """
    Check inventory and place order without OrderFacade
    """
    order = Order()
    for item in cup_of_coffee:
        # 1. Check Inventory
        if not inventory.check_stock(item, 1):
            raise pytest.fail(f"Items {item} not in inventory")

        # 2. Reduce Stock
        inventory.reduce_stock(item, 1)

        # 3. Process the order
        order.add_item(item, 1)
        order.confirm_order()

        # Check stock reduce and order confirmed
        assert inventory.check_stock(item, 4)
    assert order.status == OrderStatus.CONFIRMED
    assert order.calculate_total() == 7.5


def test_place_order_with_facade(order_facade: OrderFacade, cup_of_coffee: tuple[Item, Item, Item]):
    """
    Check inventory and place order with OrderFacade
    """
    order = order_facade.place_order(list(cup_of_coffee), 1)
    assert order.status == OrderStatus.CONFIRMED
    assert order.calculate_total() == 7.5
