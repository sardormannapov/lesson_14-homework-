a = int(input("Enter number: "))

item = 0

while item ** 2 <= a:
    item += 1
    if item ** 2 == a:
        print(f"{item} kvadrati {a}")
        print(True)
        break
else:
    print(False)
