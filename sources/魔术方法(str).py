class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return  f"student类对象,name={self.name},age={self.age}"
stu = student("李华", 22)
stu1 = student("小明", 18)
print(stu)
print(stu1)