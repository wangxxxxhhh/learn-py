def count():
    a = 0
    for sum in range(1, 101):
        if sum % 2 == 0:
            a += sum
            print(a)
count()