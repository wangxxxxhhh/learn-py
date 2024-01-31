# 常见的数据容器
# 列表
## ①列表的定义

```py
list1 = ["列表", 2, (3, "元组"), {1, "集合"}]
```
### 1、当定义空列表时可以用下面两种方法
```pycon
1变量名称 = []
2变量名称 = list()
```
### 2、列表支持重复元素、修改、下标索引。
#### 列表中有重复元素时不报错
例:
```pycon
display = ["元素1", "元素1", 3, ...]
```
#### 使用append添加元素
例:
```pycon
display.append("元素名")
```
#### 也可以直接用append向列表中追加元组,字典,集合,元组
例:
```pycon
display.append(("元组", 000, "追加的"))
display.append({"字典":1})
display.append({"集合", 1, 2})
display.append(["列表", 1])
```
#### 可以用index来查询列表中元素的下标
例:
```pycon
display.index("元素1")
```
#### 也可以用下标索引的方式修改和插入元素
修改方法如下:列表名称[下标索引] = "想要改成的元素内容"
```pycon
display[1] = "元素2"
```
插入方法:下面就是在下标索引为1的位置插入元素"元素3"
```pycon
display.index(1, "元素3")
```
### 列表的删除的三个方法
1、del 列表名称[想要删除元素的下标索引]
例:
```pycon
del display[0]
```
2、列表名称.pop(想要删除的下标索引)
例:
```pycon
display.pop(1)
```
3、列表名称.remove(想要删除元素的名字)
例:
```pycon
display.remove("元素1")
```