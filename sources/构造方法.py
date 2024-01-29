
class Student():
    def __init__(self, name, age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print('Student创建了一个类的对象')
stu = Student("李华", 18, 12345678900)
print(stu.name)
print(stu.age)
print(stu.tel)

