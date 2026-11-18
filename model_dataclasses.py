
from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: int
    name: str
    city: str
    age: int


@dataclass
class BankCard:
    card_id: int
    customer_id: int
    card_type: str
    issue_year: int


@dataclass
class CardTransaction:
    transaction_id: int
    card_id: int
    amount: int
    transaction_date: str
    country: str
    suspicious: bool
