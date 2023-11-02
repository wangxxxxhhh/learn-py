for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}\t", end='')  # end = ''不会输出换行回车符
    print()
