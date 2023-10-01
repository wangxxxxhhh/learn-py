import math

s = input("输入一个数:")
s = int(float(s))
if s >= 0:
    s = math.sqrt(s)
    print("平方根是:", s)
else:
    print("负数不能开平方根")
print("The End")









