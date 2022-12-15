from inventory_report.reports.simple_report import SimpleReport
from datetime import datetime
from collections import Counter


class CompleteReport(SimpleReport):
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

        company_item = {}
        for item in inventory:
            if item["nome_da_empresa"] in company_item:
                company_item[item["nome_da_empresa"]] += 1
            else:
                company_item[item["nome_da_empresa"]] = 1

        company_list_item = ""
        for key, value in company_item.items():
            company_list_item += f"- {key}: {value}\n"

        return (
            f"Data de fabricação mais antiga: {min_year}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_list_item}"
        )
