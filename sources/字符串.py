my_str = "itheima itcast boxuegu"
count = my_str.count("it")
print(f"一共出现了{count}个it字符")
my_str1 = my_str.replace(" ", "|")
print(f"原字符串{my_str}被替换后为{my_str1}")
my_str2 = my_str1.split("|")
print(f"{my_str1}按照|分割后的结果为{my_str2}")