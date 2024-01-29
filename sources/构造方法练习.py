class record:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
for i in range(1, 11):
    print(f"当前录入第{i}位学生信息,共需录入10位学生信息")
    stu = record(input("请输入学生姓名:"),int(input("请输入学生年龄:")), input("请输入学生地址:"))
    print(f"学生{i}信息录入完成，信息为:【学生姓名:{stu.name},年龄:{stu.age},地址{stu.address}】")

