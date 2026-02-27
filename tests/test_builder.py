import pytest

from design_pattern.builder import Product, Builder


class ConcreteBuilder(Builder):
    def __init__(self):
        self._product = None
        self.reset()

    def reset(self):
        self._product = Product()

    def get_result(self) -> Product:
        product = self._product.get_parts()
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add_part('a')
        return self

    def produce_part_b(self):
        self._product.add_part('b')
        return self

    def produce_part_c(self):
        self._product.add_part('c')
        return self


class Director:
    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self._builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        (self._builder.produce_part_a()
         .produce_part_c()
         .produce_part_a()
         .produce_part_b()
         .produce_part_a()
         )


@pytest.fixture(scope="class")
def builder() -> Builder:
    """
        Builder instance
    """
    return ConcreteBuilder()


@pytest.fixture(scope="class")
def director(builder) -> Director:
    """
        Director instance
    """
    return Director(builder)


def test_create_products_via_director_1(builder: Builder, director: Director) -> None:
    """
        Create products with builder via director
    """

    director.build_full_featured_product()
    assert builder.get_result() == ['a', 'c', 'a', 'b', 'a']
    assert builder.get_result() == []


def test_create_products_via_director_2(builder: Builder, director: Director) -> None:
    """
        Create products with builder via director
    """
    director.build_minimal_viable_product()
    assert builder.get_result() == ['a']
    assert builder.get_result() == []


def test_create_products_via_itself_1(builder: Builder) -> None:
    """
        Create products with builder via itself
    """
    (builder.produce_part_a()
     .produce_part_b()
     .produce_part_c())
    assert builder.get_result() == ['a', 'b', 'c']
    assert builder.get_result() == []
