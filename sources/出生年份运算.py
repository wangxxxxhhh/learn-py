name = input("请输入你的名字：")
age = input("输入你的年龄：")
int_age = int(float(age))
year = 2023 - int_age
print("你的名字叫：", name + "\n", "你的年龄是：", str(int_age) + "岁\n", "你出生于：", year, '年')
