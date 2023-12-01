l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []
i = 0
while i < 10:
    if l1[i] % 2 == 0:
        l2.append(l1[i])
        print(l2)
    i += 1
# if l1[1] % 2 == 0:
#     print(l1[1])
# elif l1[1] % 2 != 0:
#     print('no')