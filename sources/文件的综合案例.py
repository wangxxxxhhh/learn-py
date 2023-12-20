fr = open('C:/bill.txt', "r", encoding='UTF-8')
fw = open('C:/bill.txt.bak.txt', "w", encoding='UTF-8')
for line in fr:
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue
    else:
        fw.write(line)
        fw.write("\n")
fr.close()
fw.close()

