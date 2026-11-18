from data.basic.model_dataclasses import Customer, BankCard, CardTransaction
from data.basic.generator import (
    generate_customers,
    generate_cards,
    generate_transactions
)

customers = generate_customers(10)
cards = generate_cards(customers, 20)
transactions = generate_transactions(cards, 50)

print("ÜGYFELEK:")
for customer in customers:
    print(customer)

print("\nBANKKÁRTYÁK:")
for card in cards:
    print(card)

print("\nTRANZAKCIÓK:")
for transaction in transactions:
    print(transaction)

suspicious_transactions = [
    transaction for transaction in transactions
    if transaction.suspicious
]

print("\nÖSSZESÍTÉS:")
print("Ügyfelek száma:", len(customers))
print("Bankkártyák száma:", len(cards))
print("Tranzakciók száma:", len(transactions))
print("Csalásgyanús tranzakciók száma:",
      len(suspicious_transactions))


from data.basic.handler import csv_dict_handler

csv_dict_handler.write(customers, "output/customers.csv")
csv_dict_handler.write(cards, "output/cards.csv")
csv_dict_handler.write(transactions, "output/transactions.csv")

read_customers = csv_dict_handler.read(
    Customer, "output/customers.csv"
)
read_cards = csv_dict_handler.read(
    BankCard, "output/cards.csv"
)
read_transactions = csv_dict_handler.read(
    CardTransaction, "output/transactions.csv"
)

print("\nCSV DICT ELLENŐRZÉS:")
print("Ügyfelek:", customers == read_customers)
print("Bankkártyák:", cards == read_cards)
print("Tranzakciók:", transactions == read_transactions)


from data.basic.handler import csv_list_handler

csv_list_handler.write(customers, "output/list_customers.csv")
csv_list_handler.write(cards, "output/list_cards.csv")
csv_list_handler.write(transactions, "output/list_transactions.csv")

read_customers_list = csv_list_handler.read(
    Customer, "output/list_customers.csv"
)
read_cards_list = csv_list_handler.read(
    BankCard, "output/list_cards.csv"
)
read_transactions_list = csv_list_handler.read(
    CardTransaction, "output/list_transactions.csv"
)

print("\nCSV LIST ELLENŐRZÉS:")
print("Ügyfelek:", customers == read_customers_list)
print("Bankkártyák:", cards == read_cards_list)
print("Tranzakciók:", transactions == read_transactions_list)



from data.basic.handler import json_handler

json_handler.write(customers, "output/customers.json")
json_handler.write(cards, "output/cards.json")
json_handler.write(transactions, "output/transactions.json")

read_customers_json = json_handler.read(
    Customer, "output/customers.json"
)
read_cards_json = json_handler.read(
    BankCard, "output/cards.json"
)
read_transactions_json = json_handler.read(
    CardTransaction, "output/transactions.json"
)

print("\nJSON ELLENŐRZÉS:")
print("Ügyfelek:", customers == read_customers_json)
print("Bankkártyák:", cards == read_cards_json)
print("Tranzakciók:", transactions == read_transactions_json)


#xlsx visszaolvasás es xls mentes teszt
from data.basic.handler import xlsx_handler

xlsx_handler.write(
    customers,
    cards,
    transactions,
    "output/bankcard_data.xlsx"
)

excel_data = xlsx_handler.read("output/bankcard_data.xlsx")

print("\nEXCEL ELLENŐRZÉS:")
print("Ügyfelek:", customers == excel_data["Customers"])
print("Bankkártyák:", cards == excel_data["BankCards"])
print("Tranzakciók:", transactions == excel_data["Transactions"])
