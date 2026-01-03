import os
import csv
import string
from .Trade import *
from .Base import clear_console
from rich import *
from rich.console import *
from rich.panel import *


console = Console()


def create_ac():
    flag2 = True
    while flag2:
        console.print('''
            [u b #408FFF]Увага![/u b #408FFF]
            [i b #D3ABFF]Логін може містити лише букви та цифри[/i b #D3ABFF]
            ''', justify="center")
        new_user_login = console.input('[b #D3ABFF]Введіть логін  >>> [/b #D3ABFF]')

        # Перевірка логіну
        with open('Files/logins.csv','r',encoding='utf-8') as file:
            a = csv.DictReader(file)
            if any(i['Logins'] == new_user_login for i in a):
                console.print("Користувач вже існує",justify="center",style='red b')
                if console.input("[b #D3ABFF]Перейти до входу в акаунт ?[/b #D3ABFF] [i b #408FFF](Так/Ні)[/i b #408FFF]").lower() == 'так':
                    flag2 = False
                    enter_ac()
            elif not any(i in string.punctuation for i in new_user_login):
                flag2 = False
            else:
                console.print("Логін не відповідає вимогам!", style='red b')

        # for i in new_user[0]:
        #     if i in string.punctuation:
        #         print("Логін не відповідає вимогам!")
        #         correct = input("""
        #         Введіть логін заново
        #         Логін може містити лише букви та цифри
        #         """)
        #         new_user[0] = correct
        #         continue

    flag3 = True
    while flag3:
        console.print('''
        [u b #408FFF]Увага![/u b #408FFF]
        [i b #D3ABFF]Пароль повинен містити комбінацію літер, цифр
        Мусить мати хоча б 1 символ і велику букву і бути довжиною більше 8[/i b #D3ABFF]
        ''',justify='center')

        new_user_pass = console.input('[b #D3ABFF]Введіть пароль  >>>[/b #D3ABFF]')

        # Перевірка паролю
        if (len(new_user_pass) > 8 and any(i in string.punctuation for i in new_user_pass)
                and any(i.isupper() for i in new_user_pass) and any(i.isdigit() for i in new_user_pass)):
            flag3 = False
        else:
            console.print("Пароль не відповідає вимогам!", style='red b')

        # if (new_user_pass.isdigit() or new_user_pass.isalpha() or len(new_user_pass) < 8
        #         or not any(i.isupper() for i in new_user_pass) or not any(i in string.punctuation for i in new_user_pass)):
        #     print("Пароль не відповідає вимогам!")
        #     continue

    new_user = [new_user_login, new_user_pass, 'Common']
    with open('Files/logins.csv', 'a', newline='', encoding='utf-8') as file:
        a1 = csv.writer(file)
        a1.writerow(new_user)

    # with open('Files/logins.csv','r',encoding='utf-8') as file:
    #     a = file.read()
    # if a not in 'Files/users.csv':
    #     with open('Files/logins.csv', 'a', encoding='utf-8') as file:
    #         a1 = csv.writer(file)
    #         a1.writerow(input("Введіть пароль"))
    # else:
    #     print("користувач вже існує!")


def enter_ac():
    flag4 = True
    while flag4:
        username = console.input("[b #D3ABFF]Введіть ваш логін  >>>[/b #D3ABFF]")
        with open('Files/logins.csv', 'r', encoding='utf-8') as file:
            a = list(csv.DictReader(file))
            if any(i['Logins'] == username for i in a):
                for i in a:
                    # print(i['Logins'])
                    if username == i['Logins']:
                        passwd = console.input("[b #D3ABFF]Введіть пароль до вашого акаунту  >>>[/b #D3ABFF]")
                        if passwd == i['Passwords']:
                            console.print("Ви увійшли в акаунт!",justify="center", style='b #D3ABFF')
                            global flag
                            flag = False
                            flag4 = False
                            with open('Files/your_rights.txt', 'w', encoding='utf-8') as file:
                                file.write(i['Rights'])
                            market()
                        else:
                            console.print("Пароль невірний!",style='red b')
            else:
                console.print("Логін невірний",style='red b')
                if console.input("[b #D3ABFF]Перейти до реєстрації ?[/b #D3ABFF] [i b #408FFF](Так/Ні)[/i b #408FFF]").lower() == 'так':
                    flag4 = False
                    create_ac()


def login():
    global flag
    flag = True
    console.print('''
    [u b #408FFF]Увага![/u b #408FFF]
    [i b #D3ABFF]Ви [u]не[/u] увійшли в свій акаунт!
    Буль ласка увійдіть або зареєструйтеся!
    Натисніть [u]Enter[/u] щоб продовжити[/i b #D3ABFF]''', justify='center')
    console.input('[#D3ABFF]>>>[/#D3ABFF]')
    clear_console()
    while flag:
        console.print('''
        [b #D3ABFF][#408FFF]1[/#408FFF] - Увійти 
        [#408FFF]2[/#408FFF] - Зареєструватися[/b #D3ABFF]
        ''',justify="center")
        choice = console.input('[b #D3ABFF]Виберіть пункт[/b #D3ABFF] [#D3ABFF]>>>[/#D3ABFF]')
        clear_console()
        match choice:
            case '1':
                enter_ac()


            case '2':
                create_ac()






