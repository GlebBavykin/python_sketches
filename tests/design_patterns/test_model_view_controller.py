import pytest
from _pytest.logging import LogCaptureFixture

from design_patterns.mode_view_controller import Product, ReceiptController, ReceiptView, RecieptModel


@pytest.fixture
def product_cart() -> list[Product]:
    """ """
    return [
        Product(name="milk", quantity=3, price=5, vat=0.1),
        Product(name="sugar", quantity=10, price=1.8, vat=0.9),
        Product(name="eggs", quantity=10, price=0.5, vat=0.12),
    ]


OUTCOME = """┌────────┬────────────┬─────────┬───────┬─────────────┬─────────┐
│ name   │   quantity │   price │   vat │   total_vat │   total │
├────────┼────────────┼─────────┼───────┼─────────────┼─────────┤
│ milk   │          3 │     5   │  0.1  │         1.5 │    16.5 │
├────────┼────────────┼─────────┼───────┼─────────────┼─────────┤
│ sugar  │         10 │     1.8 │  0.9  │        16.2 │    34.2 │
├────────┼────────────┼─────────┼───────┼─────────────┼─────────┤
│ eggs   │         10 │     0.5 │  0.12 │         0.6 │     5.6 │
└────────┴────────────┴─────────┴───────┴─────────────┴─────────┘"""


@pytest.mark.parametrize("reciept", [RecieptModel()])
@pytest.mark.parametrize("pos_printer", [ReceiptView()])
@pytest.mark.parametrize("transaction", [ReceiptController()])
def test_model_view_controller(
    transaction: ReceiptController,
    reciept: RecieptModel,
    pos_printer: ReceiptView,
    product_cart: list[Product],
    caplog: LogCaptureFixture,
):
    transaction.set_reciept(reciept)
    transaction.set_printer(pos_printer)
    for product in product_cart:
        transaction.add_a_product(product)
    transaction.write_a_cheque()
    assert OUTCOME in caplog.text
