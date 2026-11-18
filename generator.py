
import random
from datetime import datetime, timedelta
from faker import Faker

from data.basic.model_dataclasses import Customer, BankCard, CardTransaction

fake = Faker("hu_HU")


def generate_customers(count: int = 100,
                       min_age: int = 18,
                       max_age: int = 80) -> list[Customer]:
    customers = []

    for i in range(count):
        customers.append(Customer(
            customer_id=i + 1,
            name=fake.name(),
            city=fake.city(),
            age=random.randint(min_age, max_age)
        ))

    return customers


def generate_cards(customers: list[Customer],
                   count: int = 200,
                   card_types: list[str] = None) -> list[BankCard]:

    if card_types is None:
        card_types = ["Visa", "Mastercard"]

    if count > 0 and not customers:
        raise ValueError("Nincs ügyfél a kártyageneráláshoz.")

    cards = []

    for i in range(count):
        customer = random.choice(customers)

        cards.append(BankCard(
            card_id=i + 1,
            customer_id=customer.customer_id,
            card_type=random.choice(card_types),
            issue_year=random.randint(2020, 2026)
        ))

    return cards


def generate_transactions(cards: list[BankCard],
                          count: int = 1000,
                          min_amount: int = 1000,
                          max_amount: int = 2000000) -> list[CardTransaction]:

    if count > 0 and not cards:
        raise ValueError("Nincs kártya a tranzakciógeneráláshoz.")

    transactions = []

    countries = ["Magyarország", "Ausztria", "Németország",
                 "Lengyelország", "USA"]

    for i in range(count):
        card = random.choice(cards)
        amount = random.randint(min_amount, max_amount)
        country = random.choice(countries)

        suspicious = amount > 1000000 or (
            country == "USA" and amount > 500000
        )

        date = datetime.now() - timedelta(
            days=random.randint(0, 365)
        )

        transactions.append(CardTransaction(
            transaction_id=i + 1,
            card_id=card.card_id,
            amount=amount,
            transaction_date=date.strftime("%Y-%m-%d"),
            country=country,
            suspicious=suspicious
        ))

    return transactions
