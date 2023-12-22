def calculate(num1, num2, operation):
    if operation == "":
        cal = num1 + num2
        print(f"两数相加的合为{cal}")
    elif operation == "-":
        cal = num1 - num2
        print(f"两数之差为{cal}")
    elif operation == "*":
        cal = num1 * num2
        print(f"两数相乘为{cal}")
    elif operation == "/":
        if num2 == 0:
            print("输入有误请重新输入")
        else:
            cal = num1 / num2
            print(f"两数相除为{cal}")
    else:
        print("输入错误请重新输入。")
calculate(6, 6, operation="")

