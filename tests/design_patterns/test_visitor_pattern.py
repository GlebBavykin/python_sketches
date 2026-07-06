import pytest
from _pytest.logging import LogCaptureFixture

from design_patterns.behavioral.visitor_pattern import (CompositeVisitor,
                                                        PackageItem,
                                                        ProductItem)


@pytest.fixture(scope="class")
def visitor() -> CompositeVisitor:
    """
    Visitor instance
    """
    return CompositeVisitor()


@pytest.fixture(scope="class")
def product() -> ProductItem:
    """
    One product
    """
    return ProductItem(price=1, weight=2)


@pytest.fixture(scope="class")
def package(product) -> PackageItem:
    """
    Package with other package and products in it
    """
    return (
        PackageItem()
        .add_item(PackageItem().add_item(product))
        .add_item(product)
        .add_item(PackageItem().add_item(product).add_item(PackageItem().add_item(product)))
    )


def test_visitor_for_composite_package(
    package: PackageItem, visitor: CompositeVisitor, caplog: LogCaptureFixture
) -> None:
    """
    Check visitor pattern: accept visitor for composite package and capture log from the console
    """
    package.accept(visitor)
    assert "Price: 4, Weight: 8" in caplog.text


def test_visitor_for_composite_product(
    product: ProductItem, visitor: CompositeVisitor, caplog: LogCaptureFixture
) -> None:
    """
    Check visitor pattern: accept visitor for composite product and capture log from the console
    """
    product.accept(visitor)
    assert "Price: 1, Weight: 2" in caplog.text
