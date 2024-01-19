import json
list1 = [{"王向辉": 1}, {"小明": 2}, {"小李": "小张"}]
json_list1 = json.dumps(list1, ensure_ascii=False)
dict1 = {"小陈": "qwer"}
json_dict1 = json.dumps(dict1, ensure_ascii=False)
s = '[{"k": "v", "k": "v"}, {"k": "v", "k": "v"}]'
l = json.loads(s)
s1 = '{"小王": 123}'
d = json.loads(s1)
print(f"列表中的内容为{json_list1},类型为{type(json_list1)}")
print(f"列表中的内容为{json_dict1},类型为{type(json_list1)}")
print(f"列表中的内容为{l},类型为{type(l)}")
print(f"列表中 的内容为{d},类型为{type(d)}")