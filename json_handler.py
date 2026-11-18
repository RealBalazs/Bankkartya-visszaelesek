
import json
from dataclasses import asdict
from pathlib import Path
from typing import Type

from data.basic.model_dataclasses import (
    Customer, BankCard, CardTransaction
)


def write(entities: list, path: str, pretty: bool = True) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            [asdict(entity) for entity in entities],
            file,
            indent=4 if pretty else None,
            ensure_ascii=False
        )


def read(entity_type: Type, path: str) -> list:
    if entity_type not in (Customer, BankCard, CardTransaction):
        raise ValueError("Ismeretlen adattípus.")

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [entity_type(**item) for item in data]
