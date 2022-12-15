from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path, type):
        if "csv" in path:
            return Inventory.open_csv(path, type)
        elif "json" in path:
            return Inventory.open_json(path, type)

    @staticmethod
    def open_csv(path, type):
        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport.generate(list(file_reader))
            elif type == "completo":
                return CompleteReport.generate(list(file_reader))
            else:
                raise ValueError("Tipo inválido")

    @staticmethod
    def open_json(path, type):
        with open(path) as file:
            file_reader = json.load(file)
            if type == "simples":
                return SimpleReport.generate(file_reader)
            elif type == "completo":
                return CompleteReport.generate(file_reader)
            else:
                raise ValueError("Tipo inválido")
