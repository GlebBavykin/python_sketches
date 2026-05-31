from typing import Protocol, Self


class Calculable(Protocol):
    """
    Common interface for Product and Package
    """

    def price(self) -> float: ...

    def weight(self) -> float: ...


class Product:
    """
    Leaf of Package class
    """

    def __init__(self, price: float, weight: float):
        self._price = price
        self._weight = weight

    @property
    def price(self) -> float:
        return self._price

    @property
    def weight(self) -> float:
        return self._weight


class Package:
    """
    Container of Product and Package
    """

    def __init__(self):
        self._products = []

    def add_item(self, product: Product | Package) -> Self:
        self._products.append(product)
        return self

    def remove_item(self, product: Product | Package) -> Self:
        self._products.remove(product)
        return self

    @property
    def price(self) -> float:
        return sum(product.price for product in self._products)

    @property
    def weight(self) -> float:
        return sum(product.weight for product in self._products)
