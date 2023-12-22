demo1_list = [1, 2, 'Python', [3, 4, 'd', 0], 5]
demo1_list.append('java')
print(f"列表追加元素'java'后变为{demo1_list}")
a = demo1_list.index([3, 4, 'd', 0])
demo1_list.remove([3, 4, 'd', 0])
demo1_list.insert(3, 34)
print(f"[3, 4, 'd', 0]元素在列表中的位置为{a},列表更改后得到的新列表为{demo1_list}")
demo1_list = demo1_list[::-1]
print(f"将列表逆置的结果为{demo1_list}")
demo1_list.pop(-1)
print(f"删除最后一个元素列表变为:{demo1_list}")
demo1_list.remove('Python')
print(f"删除元素'Python'后列表变为:{demo1_list}")