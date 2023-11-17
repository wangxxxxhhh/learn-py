def tem(num):
    print("请测量体温。")
    if num <= 37.5:
        print(f"您的体温是{num}度，体温正常可以进入。")
    else:
        print(f"您的体温是{num}度，体温过高不可进入")
tem(37)