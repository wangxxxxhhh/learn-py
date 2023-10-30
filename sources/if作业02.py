min = int(input("请输入停车分钟数:"))
a = int((min-120)//60)
if min >= 0:
    if min <= 15:
        print("现在不要你钱了")
    else:
        if 15 < min < 120:
            print("现在该收两元钱了")
        else:
            if (min - 120) % 60 > 0:
                if min >= 960:
                    print("已经最高费用50元了。")
                else:
                    print("现在需要费用:", 2+(a+1)*3)
            else:
                print("现在需要的费用为:", 2+a*3)
else:
    print("输入错误")

