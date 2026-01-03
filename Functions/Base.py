import os
import csv
import string
from .Trade import *
from .Login import login
from rich import *
from rich.console import *
from rich.panel import *

console = Console()

def clear_console():
    if os.name == 'nt':  # Для Windows

        os.system('cls')

    else:  # Для Linux і macOS

        os.system('clear')


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
    login()