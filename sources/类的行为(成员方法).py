class Student:
    name = None
    def meet(self, speak):
        print(f"你好,我是{self.name},{speak}")
stu = Student()
stu.name = "李华"
stu.meet("很高兴遇到你")