e = str(input("请输入您要输入的整数:"))
def test_def():
   if e == e[::-1]:
       print(f"输入的该整数{e}为回文数")
   else:
       print(f"输入的该整数{e}不是回文数")
test_def()