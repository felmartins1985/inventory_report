from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventory: list):
        min_year = min([item["data_de_fabricacao"] for item in inventory])
        closest_date = min(
            (
                [
                    item["data_de_validade"]
                    for item in list
                    if item["data_de_validade"]
                    > datetime.now().strftime("%Y-%m-%d")
                ]
            )
        )
        print(closest_date)
        company, _ = Counter(
            item["nome_da_empresa"] for item in inventory
        ).most_common()[0]
        return f"""
            Data de fabricação mais antiga: {min_year}
            Data de validade mais próxima: {closest_date}
            Empresa com mais produtos: {company}
        """


list = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]

print(SimpleReport.generate(list))
