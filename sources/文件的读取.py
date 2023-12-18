f = open('C:/python.txt', "r", encoding="UTF-8")
count = 0
for line in f:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "iteima":
            count += 1
print(f"出现了{count}次")
content = f.read()
count = content.count('iteima')
print(count)
f.close()