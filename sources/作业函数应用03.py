def test_def(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        print("输入的三个边长可以构成三角形。")
    else:
        print("输入的三个边长不能够构成三角形。")
test_def(1, 4, 6)

