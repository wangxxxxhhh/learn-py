money = 10000
for i in range(1, 21):
    import random
    num1 = random.randint(1, 10)
    if num1 < 5:
        print(f"员工{i}的绩效分{num1}不足，不发工资")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}满足条件，发放工资1000，还剩余工资{money}元。")
    else:
        print(f"当前余额{money}元，资金不足不足以发放工资。")
        break

