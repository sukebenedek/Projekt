import os
from function import *

def menu():
    os.system('cls')
    az = 0
    print(f"Dátum: {jumpDate(str())}\n") 
    print(f'You balance: {Mymoney()}$')
    print('1..Saját részvények megnézése')
    print('2..Részvények')
    print('3..Vásárlás vagy eladás')
    print('4..Idő ugrás')
    print('5..Árváltozás utáni összegzés')
    print('')
    print('0..Kilépés a programból')

    choice = input('\nVálasztás (0..5): ')
    while len(choice) != 1 or choice < '0' or choice > '5':
        choice = input('\nVálasztás (0..5): ')
    
    os.system('cls')
    return int(choice)
