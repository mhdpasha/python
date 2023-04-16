import sys, os

def loop():
    x = str(input("Masukan password anda: "))
    pw = x

    if len(pw) >= 6:
        print("Password anda telah tersimpan")
        sys.exit()
    else:
        print("Password anda harus 6 digit keatas!")
        loop()

x = str(input("Masukan password anda: "))
pw = x

if len(pw) >= 6:
    print("Password anda telah tersimpan")
    sys.exit()
else:
    print("Password anda harus 6 digit keatas!")
    loop()