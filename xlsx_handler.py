
from dataclasses import asdict
from pathlib import Path
from openpyxl import Workbook, load_workbook

from data.basic.model_dataclasses import (
    Customer, BankCard, CardTransaction
)


def write(customers, cards, transactions, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    workbook = Workbook()
    workbook.remove(workbook.active)

    datasets = {
        "Customers": customers,
        "BankCards": cards,
        "Transactions": transactions
    }

    for sheet_name, entities in datasets.items():
        sheet = workbook.create_sheet(sheet_name)

        if entities:
            sheet.append(list(asdict(entities[0]).keys()))

            for entity in entities:
                sheet.append(list(asdict(entity).values()))

    workbook.save(path)


def read(path):
    workbook = load_workbook(path, data_only=True)

    datasets = {
        "Customers": Customer,
        "BankCards": BankCard,
        "Transactions": CardTransaction
    }

    result = {}

    for sheet_name, entity_type in datasets.items():
        sheet = workbook[sheet_name]
        rows = sheet.iter_rows(values_only=True)
        headers = next(rows, None)

        entities = []

        if headers:
            for row in rows:
                data = dict(zip(headers, row))
                entities.append(entity_type(**data))

        result[sheet_name] = entities

    workbook.close()
    return result
