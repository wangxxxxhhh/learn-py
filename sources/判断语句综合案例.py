import random
num = random.randint(1, 10)
guess_num = int(input("输入你要猜测的数字:"))
if guess_num == num:
    print("恭喜第一次就猜对了。")
else:
    if guess_num > num:
        print("猜大了。")
    else:
        print("猜小了。")
    guess_num = int(input("输入第二次猜测的数字:"))
    if guess_num == num:
        print("恭喜第二次猜对了。")
    else:
        if guess_num > num:
            print("猜大了。")
        else:
            print("猜小了。")
    guess_num = int(input("输入第三次猜测的数字:"))
    if guess_num == num:
        print("恭喜第三次猜对了。")
    else:
        print("不好意思，三次都猜错了。")
