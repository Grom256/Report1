from Functions import *

import csv
import os


keys_log = ['Logins','Passwords','Rights']
default_log = ['admin', 'Admin228', 'Admin']

keys_cr = ['ID','Назва', 'Ціна покупки', 'Ціна продажу', 'Доступна кількість для продажу', 'Доступна кількість для покупки']
default_cr = ['1','TON', '1.2', '1.7', '120', '450']

keys_history = ['user', 'ttype', 'coinID','price','qty','suma','address']


if not os.path.exists('Files/logins.csv'):
    with open('Files/logins.csv', 'a', newline='',encoding='utf-8') as a:
        a1 = csv.writer(a)
        a1.writerows([keys_log,default_log])


if not os.path.exists('Files/crypto.csv'):
    with open('Files/crypto.csv', 'a', newline='',encoding='utf-8') as file:
        a1 = csv.writer(file)
        a1.writerows([keys_cr,default_cr])

if not os.path.exists('Files/history.csv'):
    with open('Files/history.csv','a',newline='',encoding='utf-8') as file:
        a = csv.writer(file)
        a.writerow(keys_history)

def greetings():
    logo = """

 ▄▄▄▄▄▄▄                              ▄▄▄▄▄▄▄▄▄             ▄▄       
███▀▀▀▀▀                    ██        ▀▀▀███▀▀▀             ██       
███      ████▄ ██ ██ ████▄ ▀██▀▀ ▄███▄   ███ ████▄  ▀▀█▄ ▄████ ▄█▀█▄ 
███      ██ ▀▀ ██▄██ ██ ██  ██   ██ ██   ███ ██ ▀▀ ▄█▀██ ██ ██ ██▄█▀ 
▀███████ ██     ▀██▀ ████▀  ██   ▀███▀   ███ ██    ▀█▄██ ▀████ ▀█▄▄▄ 
                 ██  ██                                              
               ▀▀▀   ▀▀                                              """
    console.print(logo, style='#408FFF')
    console.print(Panel('''
    [i u b #9523FA]Ласкаво просимо до CryptoTrade![/i u b #9523FA]
    [i #DBDBDB]Тут ви можете купити та продати свою криптовалюту
    швидко, безпечно та без зайвої мороки![/i #DBDBDB]
    [#DBDBDB]Натисніть [b #D3ABFF u i]Enter[/b #D3ABFF u i] щоб перейти до меню![/#DBDBDB]''', title='Welcome'),
                  justify='center')
    console.input('[#D3ABFF]>>>[/#D3ABFF]')
    clear_console()
    with open('Files/your_rights.txt', 'r', encoding='utf-8') as file:
        a = file.read()
        if a == 'Admin':
            admin_flag = True
            while admin_flag:
                console.print(Panel('''
                [#FFB700]
                [b #FC4F0A]1[/b #FC4F0A] -  Додати критовалюту
                [b #FC4F0A]2[/b #FC4F0A] -  Видалити криптовалюту
                [b #FC4F0A]3[/b #FC4F0A] -  Звичайне меню[/#FFB700]''',title='Адмін меню',style='#B30000 b'),justify="center")

                admin_choice = console.input('[#B30000 b]Виберіть пункт  >>> [/#B30000 b]')
                match admin_choice:
                    case '1':
                        addCrypto()
                    case '2':
                        deleteCrypto()
                    case '3':
                        admin_flag = False
                        menu()

        else:
            menu()

is_log = False
def check():
    with open('Files/logins.txt', 'r', encoding='utf-8') as file:
        a = file.read()
        if a == '':
            console.print('''
            Ви не увійшли в акаунт!
            Увійдіть або зареєструйтесь у меню!
            ''',justify="center",style='b #843EE6')
            global is_log
            is_log = False
        else:
            is_log = True

def menu():
    flag_menu = True
    while flag_menu:
        console.print(Panel('''
        [i u b #9523FA]Вітаємо у меню![/i u b #9523FA]
        [b #D3ABFF]
        [#408FFF]1[/#408FFF] - Увійти/зареєструватися
        [#408FFF]2[/#408FFF] - Преміум статус для акаунту
        [#408FFF]3[/#408FFF] - Маркет
        [#408FFF]4[/#408FFF] - Історія транзакцій
        [#408FFF]5[/#408FFF] - Вийти з програми[/b #D3ABFF]
        '''),justify="center")

        menu_choice = console.input('[b #D3ABFF]Виберіть пункт  >>> [b #D3ABFF]')
        match menu_choice:
            case '3':
                check()
                if is_log:
                    market()
            case '2':
                check()
                if is_log:
                    with open('Files/your_rights.txt', 'r', encoding='utf-8') as file:
                        a = file.read()
                        if a == 'Common':
                            status()
                        else:
                            console.print('''
                            У Вас вже є преміум статус!
                            
                            Повернення до меню...''',justify="center",style='b #D3ABFF')
                            with console.status('Завантаження...', spinner_style='b'):
                                time.sleep(3)

            case '4':
                check()
                if is_log:
                    with open('Files/logins.txt', 'r',encoding='utf-8') as file:
                        a = file.read()
                        with open('Files/history.csv','r',encoding='utf-8') as file:
                            a1 = csv.DictReader(file)
                            b = list(a1)
                            history_table = Table(header_style='b #9523FA', title='Історія Ваших транзакцій!',
                                                  title_style='b u i #250047 on #9CA3AF',
                                                  border_style='#9CA3AF', box=box.ROUNDED)
                            history_table.add_column('Користувач', style='#D3ABFF i b', justify="center")
                            history_table.add_column('Тип угоди', style='#D3ABFF i b', justify="center")
                            history_table.add_column('ID криптовалюти', style='#D3ABFF i b', justify="center")
                            history_table.add_column('Ціна', style='#D3ABFF i b', justify="center")
                            history_table.add_column('Кількість', style='#D3ABFF i b', justify="center")
                            history_table.add_column('Сума', style='#D3ABFF i b', justify="center")
                            history_table.add_column('Адреса гаманця', style='#D3ABFF i b', justify="center")
                            if a == 'admin':
                                for i in b:
                                    history_table.add_row(i['user'], i['ttype'], i['coinID'], i['price'], i['qty'],
                                                          i['suma'], i['address'])
                            else:
                                for i in b:
                                    if i['user'] == a:
                                        history_table.add_row(i['user'],i['ttype'],i['coinID'],i['price'],i['qty'], i['suma'],i['address'])
                    console.print(history_table,justify="center")
                    console.input('[b #D3ABFF]Натисніть Enter щоб продовжити  >>>[/b #D3ABFF]')
            case '1':
                login()
            case '5':
                flag_menu = False


greetings()