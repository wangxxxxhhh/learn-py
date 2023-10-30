weight = int(input("请输入邮件的重量："))
a = int((weight-1000) // 500)
b = input("是否需要加急(输入y表示需要，n表示不要):")
if b == "n":
    print('不需要加急')
    if weight <= 1000:
        print("需要收取12元费用")
    else:
        if (weight-1000)%500>0:
            print("需要的费用为：",12+(a+1)*4)
        else:
            print("需要的费用为：",12+a*4)
else:
    if weight <= 1000:
        print("需要收取17元费用")
    else:
        if (weight-1000)%500>0:
            print("需要的费用为：",17+(a+1)*4)
        else:
            print("需要的费用为：",17+a*4)