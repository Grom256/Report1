from rich.console import *
from rich.panel import *
from rich import *
from rich.color import *
import csv
console = Console()

def addCrypto():
    values = console.input("Введіть ID, назву, ціну покупки, ціну продажу, доступну кількість для продажу і доступну кількість для покупки").split()
    with open('Files/crypto.csv', 'a', newline='', encoding='utf-8') as file:
        a = csv.writer(file)
        a.writerow(values)

def deleteCrypto():
    choiceID = console.input("Введіть ID монети, яку хочете видалити")
    with open('Files/crypto.csv', 'r', encoding='utf-8') as file:
        a = csv.DictReader(file)
        b = list(a)
        new_crypto_file = [i for i in b if i['ID'] != choiceID]
    with open('Files/crypto.csv', 'w', newline='', encoding='utf-8') as file:
        a = csv.DictWriter(file, fieldnames=b[0].keys())
        a.writeheader()
        a.writerows(new_crypto_file)


