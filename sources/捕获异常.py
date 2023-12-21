# 基本捕获异常
try:
    f = open("C:/pyfile/bug.txt", "r", encoding="UTF-8")
except:
    f = open("C:/pyfile/bug.txt", 'w', encoding="UTF-8")
finally:
    f.close()

# 捕获全部异常
try:
    print(name)
except Exception as e:
    print("出现了异常")