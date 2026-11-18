
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
        writer = csv.writer(file, delimiter=";")

        writer.writerow(asdict(entities[0]).keys())

        for entity in entities:
            writer.writerow(asdict(entity).values())


def read(entity_type: type, path: str) -> list:
    entities = []

    with open(path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader, None)

        for row in reader:
            if entity_type == Customer:
                entity = Customer(
                    int(row[0]),
                    row[1],
                    row[2],
                    int(row[3])
                )

            elif entity_type == BankCard:
                entity = BankCard(
                    int(row[0]),
                    int(row[1]),
                    row[2],
                    int(row[3])
                )

            elif entity_type == CardTransaction:
                entity = CardTransaction(
                    int(row[0]),
                    int(row[1]),
                    int(row[2]),
                    row[3],
                    row[4],
                    row[5] == "True"
                )

            else:
                raise ValueError("Ismeretlen adattípus.")

            entities.append(entity)

    return entities
