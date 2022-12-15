from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",")
            print(file_reader)
            if type == "simples":
                return SimpleReport.generate(file_reader)
            elif type == "completo":
                return CompleteReport.generate(file_reader)


print(Inventory.import_data("inventory_report/data/inventory.csv", "simples"))