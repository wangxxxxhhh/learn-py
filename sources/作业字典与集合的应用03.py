list = [10000, 5200, 4700, 3860, 1200, 8500]
print(f"员工月薪数据为:{list}")
list.insert(2, 4500)
print(f"更新后列表的内容为:{list}")
list.pop(4)
print(f"删除列表中第五个薪水数据后的结果为:{list}")
for i in list:
    if i < 5000:
        x = list.index(i)
        list[x] = 5000
        print(f"索引为{x}的员工月薪小于5000,修改后的列表为:{list}")
new_dict = {"a1": {'姓名': '王保华',
                   '月薪': 10000},
            "a2": {'姓名': '李伟新',
                   '月薪': 5200},
            "a3": {'姓名': '张强',
                   '月薪': 4700},
            "a4": {'姓名': '张明',
                   '月薪': 3860},
            "a5": {'姓名': '陈鑫',
                   '月薪': 1200},
            "a6": {'姓名': '李牧',
                   '月薪': 8500},
            }
print(f"员工的数据为:{new_dict}")
new_dict['a7'] = {'姓名': '李梅', '月薪': 9000}
new_dict['a4'] = {'姓名': '张明', '月薪': 4900}
print(f"将字典修改后变为:{new_dict}")
new_dict.pop('a4')
print(f"将字典删除'a4'员工信息后员工信息变为{new_dict}")
