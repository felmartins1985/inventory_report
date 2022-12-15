from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventory: list):
        min_year = min([item["data_de_fabricacao"] for item in inventory])
        closest_date = min(
            [
                item["data_de_validade"]
                for item in inventory
                if item["data_de_validade"]
                > datetime.now().strftime("%Y-%m-%d")
            ]
        )
        company, _ = Counter(
            item["nome_da_empresa"] for item in inventory
        ).most_common()[0]
        return (
            f"Data de fabricação mais antiga: {min_year}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )
