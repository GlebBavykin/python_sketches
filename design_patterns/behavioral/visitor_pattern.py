import logging
from typing import Protocol

from design_patterns.structural.composite import Package, Product

logger = logging.getLogger(__name__)


class Visitor(Protocol):
    """
    Visitor interface
    """

    def visit_package(self, package: Package) -> None: ...

    def visit_product(self, product: Product) -> None: ...


class CompositeVisitor(Visitor):
    """
    Concrete Visitor
    """

    def visit_package(self, package: Package) -> None:
        logger.info(package)

    def visit_product(self, product: Product) -> None:
        logger.info(product)


class Item(Protocol):
    """
    Item interface
    """

    def accept(self, visitor: Visitor) -> None: ...


class ProductItem(Item, Product):
    """
    Product
    """

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_product(self)


class PackageItem(Item, Package):
    """
    A Package for products and another packages
    """

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_package(self)
