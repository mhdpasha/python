import sys

# defaul val
arr = [0, 1, 2]
print(arr)

# main
user = int(input("Masukan angka yang ingin ditambahkan: "))
arr.append(user)
print(arr)

# return
amount = len(arr)
if amount > 3:
    sys.exit()