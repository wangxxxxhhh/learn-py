money = 5000000
name = None
name = input("请输入您的姓名:")


def query(judge):
    if judge:
        print("--------查询余额--------")
    print(f"{name}，您好，您的余额还剩{money}元。")


def saving(num):# saving英语存款
    global money
    money +=num
    print("--------存款--------")
    print(f"{name}，您好，您存款成功{num}元。")
    query(False)


def withdrawal(num):# withdrawal英语取款
    global money
    money -= num
    print("--------取款--------")
    print(f"{name}，您好，您取款成功{num}元。")
    query(False)
def main():
    print("--------主菜单--------")
    print(f"{name}，您好欢迎来到银行，请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择:")
while True:
    key_board_input = main()
    if key_board_input == "1":
        query(True)
        continue
    elif key_board_input == "2":
        num = int(input("您需要存款多少钱？请输入:"))
        saving(num)
        continue
    elif key_board_input == "3":
        num = int(input("您需要取款多少？请输入:"))
        withdrawal(num)
        continue
    else:
        print("程序退出")
        break


