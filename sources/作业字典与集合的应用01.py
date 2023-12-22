dict_demo = {"k1": "v1", "k2": "v2", "k3": "v3"}
for key in dict_demo:
    print(f"遍历出所有的键为:{key}")
for value in dict_demo.values():
    print(f"在字典中遍历出来的值为{value}")
for key, value in dict_demo.items():
    print(f"在字典中遍历出的键值对为:{key, value}")
dict_demo["k4"]="v4"
dict_demo["k5"]="v6"
print(f"在字典中添加两个键值对后的结果为:{dict_demo}")
dict_demo["k5"]="v5"
print(f'将字典中的键值对更改后为{dict_demo}')
dict_demo.clear()
print(f"将字典清空后内容为{dict_demo},类型为{type(dict_demo)}")
