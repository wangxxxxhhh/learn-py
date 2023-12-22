li_num1 = [4, 5, 2, 7]
li_num2 = [3, 6]
for i in li_num2:
    li_num1.append(i)
    li_num1 = sorted(li_num1, reverse=True)
    # li_num1 = li_num1[::-1]
    print(f"两个列表合并后的元素为{li_num1}")
