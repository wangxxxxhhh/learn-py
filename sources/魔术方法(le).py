class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __le__(self, others):
        return self.age <= others.age
stu1 = student("李华", 22)
stu2 = student("小明", 18)
print(stu1 >= stu2)
print(stu1 <= stu2)
