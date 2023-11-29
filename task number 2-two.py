a = [1, 2, 2, 2, 3, 5, 5, 7, 2]
b = int(input("Son kiriting: "))
for x in a:
    c = a.count(b)
    print(c)
    print(f"{b} soni {c} martta qaytarilgan")
    break