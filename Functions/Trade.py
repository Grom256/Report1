import csv
import os
from rich import *
from rich.panel import *
from rich.console import *
from rich.table import *
from rich.spinner import *
import time

from .Base import clear_console

console = Console()


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
            if a == 'Premium' or 'Admin':
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
                [i u b #9523FA]Що бажаєте зробити ?[/i u b #9523FA]
                
                [b #D3ABFF][#408FFF]1[/#408FFF] - Купити
                [#408FFF]2[/#408FFF] - Продати[/b #D3ABFF]''', justify="center")
                choice_trade = console.input('[b #D3ABFF]Виберіть пункт  >>> [/b #D3ABFF]')
                match choice_trade:
                    case '1':
                        buy()
                    case '2':
                        with open('Files/your_rights.txt','r', encoding='utf-8') as file1:
                            a1 = file1.read()
                            if a1 == 'Common':
                                console.print(Panel('''
                                На жаль, вам не доступна функція продажу нам вашої криптовалюти, 
                                отримайте преміум статус, щоб її розблокувати.
                                
                                [b #D3ABFF]Перейти до отримання Premium статусу ?[b #D3ABFF][i b #408FFF](Так/Ні)[/i b #408FFF]
                                '''),justify="center")
                                status_choice = console.input('[b #D3ABFF]Виберіть пункт >>> [/b #D3ABFF]').lower()
                                match status_choice:
                                    case 'так':
                                        status()
                                    case _:
                                        console.print('Повернення назад до маркету', justify="center", style='b #D3ABFF')
                                        market()

                            elif a1 == 'Premium' or 'Admin':
                                sell()


def status():
    console.print(Panel('''
    [b]Ціна Premium статусу для акаунту - $199
    Статус дається пожитєво[/b]
    
    [b #D3ABFF][#408FFF]1[/#408FFF] - продовжити
    [#408FFF]2[/#408FFF] - повернутися до маркету[/b #D3ABFF]
    ''',title='Premium'),justify='center')
    status_choice = console.input('[b #D3ABFF]Виберіть пункт  >>> [/b #D3ABFF]')
    flag_status = True
    match status_choice:
        case '1':
            while flag_status:
                card = console.input('[b #D3ABFF]Введіть дані вашої банківської карти [#408FFF](Номер, термін дії і CVV)[/#408FFF]  >>> [b #D3ABFF]').split()
                if len(card[0]) != 16 or not card[0].isdigit() or len(card[2]) != 3 or not card[2].isdigit():
                    console.print('Будь ласка, не старайтесь обманути систему!',justify="center",style='b u #D3ABFF')
                else:
                    flag_status = False
                    with open('Files/logins.csv', 'r', encoding='utf-8') as file:
                        a = csv.DictReader(file)
                        b = list(a)
                        new_logins = []
                        with open('Files/logins.txt', 'r', encoding='utf-8') as file:
                            a = file.read()
                            for i in b:
                                if i['Logins'] == a:
                                    i['Rights'] = 'Premium'
                                new_logins.append(i)
                            console.print(Panel('''
                            Тепер ваш акаунт має Premium статус!
                            Приємного користування!
                            ''',title='Вітаємо!',style='b #D3ABFF', border_style='#E7E7E7'),justify='center')

                    with open('Files/logins.csv','w',newline='', encoding='utf-8') as file:
                        a = csv.DictWriter(file, fieldnames=b[0].keys())
                        a.writeheader()
                        a.writerows(new_logins)

        case '2':
            market()
def buy():
    flag5 = True
    while flag5:
        try:
            how_many = float(console.input("[b #D3ABFF]Введіть кількість криптовалюти, яку хочете купити  >>> [/b #D3ABFF]"))
        except:
            console.print('Щось пішло не так, можливо ви ввели не число',justify='center',style='[b red]')
        else:
            flag5 = False


    with open('Files/crypto.csv','r', encoding='utf-8') as file:
        a = csv.DictReader(file)
        b = list(a)
        for i in b:
            # if any(float(i['Доступна кількість для продажу']))
            if i['ID'] == choice_market and float(i['Доступна кількість для продажу']) >= how_many:

                console.print(f'''
                [b #D3ABFF]Сума до оплати: [#408FFF]{float(i['Ціна продажу'])*how_many}[/#408FFF]
                
                
                Заповніть необхідні дані:[/b #D3ABFF]''',justify="center")
                flag6 = True
                while flag6:
                    card = console.input('[b #D3ABFF]Введіть дані вашої банківської карти (Номер, термін дії і CVV)  >>> [/b #D3ABFF]').split()
                    console.print(Panel('''
                    Ми [u]НЕ беремо[/u] на себе відповідальність за будь які проблеми, які виникли через недбалість користувача. 
                    Наприклад, якщо криптовалюта не надійде користувачу через неправильну адресу, компенсація не надається!
                    ''',style='dim'),justify="center",style='dim')
                    address = console.input('[b #D3ABFF]Введіть адресу, на яку буде зараховано криптовалюту  >>> [b #D3ABFF]')
                    with console.status('Обробка...',spinner_style='b'):
                        time.sleep(4)
                    if len(card[0]) != 16 or not card[0].isdigit() or len(card[2]) != 3 or not card[2].isdigit():
                        console.print('Будь ласка, не старайтесь обманути систему!',justify="center",style='b red')
                    else:
                        for i1 in b:
                            if i1['ID'] == choice_market:
                                i1['Доступна кількість для продажу'] = float(i1['Доступна кількість для продажу'])-how_many
                            b1 = [i1]
                        print(b1)

                        with open('Files/logins.txt', 'r', encoding='utf-8') as file:
                            a = file.read()
                            history(a,'buy',choice_market,i['Ціна продажу'],how_many,float(i['Ціна продажу'])*how_many,address)

                        with open('Files/crypto.csv','w', newline='', encoding='utf-8') as file1:
                            a = csv.DictWriter(file1, fieldnames=b[0].keys())
                            a.writeheader()
                            a.writerows(b1)


                        console.print(Panel('''
                        [b #9523FA]Вітаю!
                        Замовлення виконанно успішно![/b #9523FA]
                        
                        [b #D3ABFF][i]Дякуємо, що вибрали CryproTrade![/i]
                        
                        [#408FFF]1[/#408FFF] - повернутися до маркету
                        [#408FFF]2[/#408FFF] - вийти у меню[/b #D3ABFF]'''),justify="center")

                        finish_choice = console.input('[b #D3ABFF]Виберіть пункт  >>> [/b #D3ABFF]')
                        match finish_choice:
                            case '1':
                                market()
                            case '2':
                                pass

                        flag6 = False




def sell():
    flag7 = True
    while flag7:
        try:
            how_many = float(console.input("[b #D3ABFF]Введіть кільсть криптовалюти, яку хочете продати  >>> [/b #D3ABFF]"))
        except:
            console.print('Щось пішло не так, можливо ви ввели не число',justify="center",style='red b')
        else:
            flag7 = False

    with open('Files/crypto.csv', 'r', encoding='utf-8') as file:
        a = csv.DictReader(file)
        b = list(a)
        for i in b:
            if i['ID'] == choice_market and float(i['Доступна кількість для покупки']) >= how_many:

                console.print(f'''
                    [b #D3ABFF]Сума, яка прийде на ваш рахунок: [#408FFF]{i['Ціна покупки'] * how_many}[/#408FFF]


                    Заповніть необхідні дані:[/b #D3ABFF]''')
                flag6 = True
                while flag6:
                    card = console.input('[b #D3ABFF]Введіть номер вашої банківської карти  >>> [/b #D3ABFF]')
                    console.print(Panel('''
                        Ми [u]НЕ беремо[/u] на себе відповідальність за будь які проблеми, які виникли через недбалість користувача. 
                        Наприклад, якщо кошти не надійшли користувачу через неправильний номер, компенсація не надається!
                        ''', style='dim'),justify="center",style='dim')
                    # address = console.input('Введіть адресу, на яку буде зараховано криптовалюту')
                    if len(card) != 16 or not card.isdigit():
                        console.print('Будь ласка, введіть номер банківської карти!  >>>',justify="center", style='red b')
                    else:
                        b1 = []
                        for i1 in b:
                            if i1['ID'] == choice_market:
                                i1['Доступна кількість для покупки'] = float(
                                    i1['Доступна кількість для покупки']) - how_many
                            b1.append(i1)
                        print(b1)

                        with open('Files/logins.txt', 'r', encoding='utf-8') as file:
                            a = file.read()
                            history(a,'sell',choice_market,i['Ціна покупки'],how_many,float(i['Ціна покупки'])*how_many)

                        with open('Files/crypto.csv', 'w', newline='', encoding='utf-8') as file1:
                            a = csv.DictWriter(file1, fieldnames=b[0].keys())
                            a.writeheader()
                            a.writerows(b1)

                        console.print(Panel('''
                        [b #9523FA]Вітаю!
                        Замовлення виконанно успішно![/b #9523FA]
                        
                        [b #D3ABFF][i]Дякуємо, що вибрали CryproTrade![/i]
                        
                        [#408FFF]1[/#408FFF] - повернутися до маркету
                        [#408FFF]2[/#408FFF] - вийти з програми[b #D3ABFF]'''),justify='center')

                        finish_choice = console.input('[b #D3ABFF]Виберіть пункт  >>> [/b #D3ABFF]')
                        match finish_choice:
                            case '1':
                                market()
                            case '2':
                                pass

                        flag6 = False

            # else:
            #     console.print('На жаль, на данний момент ми не можемо купити стільки вибраної криптовалюти', justify="center", style='red b')
            #     trade()


def history(user,ttype,coinID,price,qty,suma,address=''):
    row = [user,ttype,coinID,price,qty,suma,address]
    with open('Files/history.csv','a',newline='',encoding='utf-8') as file:
        a = csv.writer(file)
        a.writerow(row)