import my_utils.str_until
from my_utils import file_util
print(my_utils.str_until.str_reverse("辉向王"))
print(my_utils.str_until.substr("王向辉真帅", 1, 5))
print(my_utils.file_util.print_file_info("C:/pyfile/邀请函.txt"))
print(my_utils.file_util.append_to_file("C:/pyfile/邀请函.txt", "大帅逼王向辉"))