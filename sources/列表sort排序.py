one_list = [["A", 22], ["B", 33], ["C", 11]]

def sort_list(compare):
    return compare[0]
one_list.sort(key=sort_list, reverse=True)
print(one_list)
one_list.sort(key=lambda element: element[1], reverse=False)
print(one_list)