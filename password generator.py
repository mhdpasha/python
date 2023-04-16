#Random Password Generator by Pasha
import numbers
import random

def errLoop():
    digit = int(input("Jumlah karakter password    : "))
    if digit >= 6:
        passRand(digit)
    else:
        print("Password anda harus 6 digit keatas!")
        errLoop()

def passRand(digit):
    lowerCase = "abcdefghijklmnopqrstuvwxyz" 
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers   = "0123456789"
    symbols   = "@#$%&?;"

    passElement = lowerCase+upperCase+numbers+symbols
    passLength  = digit

    password = "".join(random.sample(passElement, passLength))
    print("Password baru anda adalah   : " + password)

#Main
digit = int(input("Jumlah karakter password    : "))
if digit >= 6:
    passRand(digit)
else:
    print("Password anda harus 6 digit keatas!")
    errLoop()