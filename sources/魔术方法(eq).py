class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
stu = student("李华", 19)
stu1 = student("小明", 18)
print(stu == stu1)