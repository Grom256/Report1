from Functions import *

import csv
import os


keys = ['Logins','Passwords','Rights']
default = ['admin', 'Admin228', 'Admin']

if not os.path.exists('Files/logins.csv'):
    with open('Files/logins.csv', 'a', newline='',encoding='utf-8') as a:
        a1 = csv.writer(a)
        a1.writerows([keys,default])
greetings()