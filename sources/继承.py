class phone:
    producer = "小米"

    def call_by_4g(self):
        print("正在使用4g网络")

    def id(self):
        print("id编码是666")


class new_phone(phone):
    def call_by_5g(self):
        print(f"厂商是{super().producer}")
        phone.call_by_4g(self)
        super().id()
        print("正在使用5g通话")


New_phone = new_phone()
new_phone.call_by_5g()
