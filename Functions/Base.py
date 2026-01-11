import os
import csv
import string
from rich import *


def clear_console():
    if os.name == 'nt':  # Для Windows

        os.system('cls')

    else:  # Для Linux і macOS

        os.system('clear')


