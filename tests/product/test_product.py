from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "Alexa",
        "Amazon",
        "15/12/2022",
        "15/12/2023",
        "123456789",
        "Armazenar em local seco",
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "Alexa"
    assert produto.nome_da_empresa == "Amazon"
    assert produto.data_de_fabricacao == "15/12/2022"
    assert produto.data_de_validade == "15/12/2023"
    assert produto.numero_de_serie == "123456789"
    assert produto.instrucoes_de_armazenamento == "Armazenar em local seco"
