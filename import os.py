import os
import math

def czy_parzysta(liczba):
    if liczba%2==0:
        print('m')
    else:
        print('k')

def kto(p):
    sprawdzenie = math.floor(p / 10)%10
    czy_parzysta(sprawdzenie)

pesel = int(input('wpisz nr pesel: '))
kto(pesel)
os.system("pause")