import pytest

from design_patterns.structural.composite import Package, Product


@pytest.fixture(scope="class")
def product() -> Product:
    """
    One product
    """
    return Product(price=1, weight=2)


@pytest.fixture(scope="class")
def package(product) -> Package:
    """
    Package with other package and products in it
    """
    return (
        Package()
        .add_item(Package().add_item(product))
        .add_item(product)
        .add_item(Package().add_item(product).add_item(Package().add_item(product)))
    )


def test_calculate_composite(package: Package) -> None:
    """
    Calculate sum of products
    """
    assert package.price == 4
    assert package.weight == 8


def test_remove_product_from_composite(package: Package, product: Product) -> None:
    """
    Calculate sum of products
    """
    package.remove_item(product)
    assert package.price == 3
    assert package.weight == 6
