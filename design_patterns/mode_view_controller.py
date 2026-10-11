import logging
from dataclasses import astuple, dataclass, field
from typing import Optional

from tabulate import tabulate

logger = logging.getLogger(__name__)


@dataclass
class Product:
    """
    A product behind the cash register
    """

    name: str
    quantity: int
    price: float
    vat: float
    total_vat: float = field(init=False)
    total: float = field(init=False)

    def __post_init__(self):
        """
        Compute total_vat and total after init
        """
        self.total_vat = self.price * self.vat * self.quantity
        self.total = (self.price * self.quantity) + self.total_vat


class RecieptModel:
    """
    Shopping cart receipt
    """

    def __init__(self):
        self._products = []

    def add_a_product(self, product: Product):
        """
        Add a product to the receipt
        """
        self._products.append(product)

    def get_products(self):
        """
        Get all products from the receipt
        """
        return self._products

    def remove_a_product(self, product: Product):
        """
        Remove a product from the receipt
        """
        self._products.remove(product)


class ReceiptView:
    """
    Receipt for Point of Sale printer
    """

    def print(self, products: list[Product]):
        """
        Print the receipt table on printer
        """
        headers = ["name", "quantity", "price", "vat", "total_vat", "total"]
        table = [astuple(product) for product in products]
        logger.info(tabulate(table, headers=headers, tablefmt="simple_grid"))


class ReceiptController:
    """
    Transaction at point of sale
    """

    def __init__(self):
        self._model: Optional[RecieptModel] = None
        self._view: Optional[ReceiptView] = None

    def set_printer(self, view: ReceiptView):
        """
        Set a point of sale printer
        """
        self._view = view

    def set_reciept(self, model: RecieptModel):
        """
        Set a reciept
        """
        self._model = model

    def write_a_cheque(self):
        """
        Print a cheque
        """
        if self._view and self._model:
            self._view.print(self._model.get_products())
        else:
            raise ValueError

    def add_a_product(self, product: Product):
        """
        Add a product to the receipt
        """
        if self._model:
            self._model.add_a_product(product)
        else:
            raise ValueError

    def remove_a_product(self, product: Product):
        """
        Remove a product from the receipt
        """
        if self._model:
            self._model.remove_a_product(product)
        else:
            raise ValueError
