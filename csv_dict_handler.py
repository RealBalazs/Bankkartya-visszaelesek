
import csv
from dataclasses import asdict
from pathlib import Path

from data.basic.model_dataclasses import (
    Customer, BankCard, CardTransaction
)


def write(entities: list, path: str) -> None:
    if not entities:
        raise ValueError("A lista nem lehet üres.")

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        field_names = list(asdict(entities[0]).keys())

        writer = csv.DictWriter(
            file,
            fieldnames=field_names,
            delimiter=";"
        )

        writer.writeheader()

        for entity in entities:
            writer.writerow(asdict(entity))


def read(entity_type: type, path: str) -> list:
    entities = []

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            if entity_type == Customer:
                entity = Customer(
                    customer_id=int(row["customer_id"]),
                    name=row["name"],
                    city=row["city"],
                    age=int(row["age"])
                )

            elif entity_type == BankCard:
                entity = BankCard(
                    card_id=int(row["card_id"]),
                    customer_id=int(row["customer_id"]),
                    card_type=row["card_type"],
                    issue_year=int(row["issue_year"])
                )

            elif entity_type == CardTransaction:
                entity = CardTransaction(
                    transaction_id=int(row["transaction_id"]),
                    card_id=int(row["card_id"]),
                    amount=int(row["amount"]),
                    transaction_date=row["transaction_date"],
                    country=row["country"],
                    suspicious=row["suspicious"] == "True"
                )

            else:
                raise ValueError("Ismeretlen adattípus.")

            entities.append(entity)

    return entities
