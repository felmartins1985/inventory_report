from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "Alexa",
        "Amazon",
        "15/12/2022",
        "15/12/2023",
        "123456789",
        "Armazenar em local seco",
    )
    assert ("Alexa" in produto.__repr__()) is True
    assert ("Amazon" in produto.__repr__()) is True
    assert ("15/12/2022" in produto.__repr__()) is True
    assert ("15/12/2023" in produto.__repr__()) is True
    assert ("Armazenar em local seco" in produto.__repr__()) is True
