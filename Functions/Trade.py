import csv
import os
from rich import *
from rich.panel import *
from rich.console import *
from rich.table import *

from .Base import clear_console

console = Console()

keys = ['ID','Назва', 'Ціна покупки', 'Ціна продажу', 'Доступна кількість для продажу', 'Доступна кількість для покупки']
default = ['1','TON', '1.2', '1.7', '120', '450']
if not os.path.exists('Files/crypto.csv'):
    with open('Files/crypto.csv', 'a', newline='',encoding='utf-8') as file:
        a1 = csv.writer(file)
        a1.writerows([keys,default])

def market():
    with open('Files/your_rights.txt', 'r', encoding='utf-8') as file:
        a = file.read()
        with open('Files/crypto.csv', 'r', encoding='utf-8') as file1:
            a1 = csv.DictReader(file1)
            table = Table(header_style='b #9523FA', title='Market', title_style='b u i #250047 on #9CA3AF',
                          border_style='#9CA3AF', box=box.ROUNDED)
            table.add_column('№', style='#D3ABFF i b', justify="center")
            table.add_column('Назва', style='#D3ABFF i b', justify="center")
            table.add_column('Ціна (покупка)', style='#D3ABFF i b', justify="center")
            table.add_column('Доступна кількість для покупки', style='#D3ABFF i b', justify="center")
            if a == 'Premium':
                table.add_column('Ціна (продаж)', style='#D3ABFF i b', justify="center")
                table.add_column('Доступна кількість для продажу', style='#D3ABFF i b', justify="center")
            for i in a1:
                if a == 'Common':
                    table.add_row(i['ID'],i['Назва'], i['Ціна продажу'], i['Доступна кількість для продажу'])

                elif a == 'Premium' or 'Admin':
                    table.add_row(i['ID'], i['Назва'], i['Ціна продажу'], i['Доступна кількість для продажу'],
                                  i['Ціна покупки'], i['Доступна кількість для покупки'])

                # elif a == 'Admin':
                #     print(i)
                #     #адміну і так норм

            console.print(table, justify="center")
    global choice_market
    choice_market = console.input("[#D3ABFF b]Введіть номер криптовалюти, яка вас зацікавила  >>> [/#D3ABFF b]")
    trade()


def trade():
    with open('Files/crypto.csv','r',encoding='utf-8') as file:
        a = csv.DictReader(file)
        for i in a:
            if i['ID'] == choice_market:
                clear_console()
                console.print('''
                Що бажаєте зробити ?
                1 - Купити
                2 - Продати''')
                choice_trade = console.input('Виберіть пункт  >>>')
                match choice_trade:
                    case '1':
                        buy()
                    case '2':
                        with open('Files/your_rights.txt','r', encoding='utf-8') as file1:
                            a1 = file1.read()
                            if a1 == 'Common':
                                console.print('''
                                На жаль, вам не доступна функція продажу нам вашої криптовалюти, 
                                отримайте преміум статус, щоб її розблокувати.
                                
                                Перейти до отримання Premium статусу ?(Так/Ні)
                                ''')
                                status_choice = console.input('Виберіть пункт >>>').lower()
                                match status_choice:
                                    case 'так':
                                        status()
                                    case _:
                                        console.print('Повернення назад до маркету')
                                        market()

                            elif a1 == 'Premium' or 'Admin':
                                sell()


def status():
    pass
def buy():
    flag5 = True
    while flag5:
        try:
            how_many = float(console.input("Введіть кільсть криптовалюти, яку хочете купити"))
        except:
            console.print('Щось пішло не так, можливо ви ввели не число')
        else:
            flag5 = False

    with open('Files/crypto.csv','w+', encoding='utf-8') as file:
        a = csv.DictReader(file)
        for i in a:
            if i['ID'] == choice_market and i['Доступна кількість для продажу'] <= how_many:
                console.print("Тепер заповніть необхідні дані:")
                flag6 = True
                while flag6:
                    card = console.input('Введіть дані вашої банківської карти (Номер, термін дії і CVV)').split()
                    console.print('''
                    Ми [u]НЕ беремо[/u] на себе відповідальність за будь які проблеми, які виникли через недбалість користувача. 
                    Наприклад, якщо криптовалюта не надійде користувачу через неправильну адресу, компенсація не надається!
                    ''',style='dim')
                    adress = console.input('Введіть адресу, на яку буде зараховано криптовалюту')
                    if len(card[0]) != 16 or not card[0].isdigit() or len(card[2]) != 3 or not card[2].isdigit():
                        console.print('Будь ласка, не старайтесь обманути систему!')
                    else:
                        console.print('''
                        Вітаю!
                        Замовлення виконанно успішно!
                        
                        Дякуємо, що вибрали CryproTrade!''')

                        flag6 = False

            else:
                console.print('На жаль, у нас на данний момент немає стільки вибраної криптовалюти')
                trade()



def sell():
    pass