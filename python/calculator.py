#Func, read vertically
def calc(user, num1, num2):
    if user == 1:
        sum = num1+num2
        print("Hasilnya adalah", sum)
    elif user == 2:
        sum = num1-num2
        print("Hasilnya adalah", sum)
    elif user == 3:
        sum = num1/num2
        print("Hasilnya adalah", sum)
    elif user == 4:
        sum = num1*num2
        print("Hasilnya adalah",sum)
    else:
        print("Dikasih 1 - 4 malah pilih yg laen tolol")

#Int main
num1 = int(input("Masukan angka 1: "))
num2 = int(input("Masukan angka 2: "))

user = int(input("Masukan jenis operasi - 1(+), 2(-), 3(:), 4(x): "))
calc(user, num1, num2)