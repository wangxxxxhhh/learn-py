import random
num = random.randint(1,100)
count = 0
flag = True
while flag:
    guess_num = int(input("输入一个数字:"))
    count += 1
    if guess_num == num:
        print("猜对了")
        flag = False
    else:
        if guess_num > num:
            print("猜大了。")
        else:
            print("猜小了。")
print("总共猜测了{count}次")

