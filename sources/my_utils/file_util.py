def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(f"文件中的所有内容如下:{content}")
    except Exception as e:
        print(f'程序出现错误了，原因是{e}')
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()
# if __name__ == '__main__':
#     print(print_file_info("C:/pyfile/邀请函.txt"))
#     print(append_to_file("C:/pyfile/邀请函.txt", "1111"))