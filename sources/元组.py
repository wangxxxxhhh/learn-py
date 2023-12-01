t1 = ('周杰伦', 11, ["football", "music"])
index = t1.index(11)
print(f"年龄的下标位置为{index}")
age = t1[0]
print(f"学生的姓名为:{age}")
t1[2][0] = "cording"
print(f"修改后的元组为{t1}")
