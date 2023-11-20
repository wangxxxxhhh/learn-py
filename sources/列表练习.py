age_list = [21, 25, 21, 23, 22, 20]
age_list.append(31)
print(f"加入元素31后列表中的元素为:{age_list}")
age_list2 = [29, 33, 30]
age_list.extend(age_list2)
print(f"追加新列表{age_list2}后的元素为:{age_list}")
count = age_list[0]
print(f"在列表中取出的元素为{count}")
count = age_list[-1]
print(f"在列表中取出的元素为{count}")
sit = age_list.index(31)
print(f"列表{age_list}中元素31的下标位置为{sit}")
print(f"列表剩余的元素为{age_list}")
