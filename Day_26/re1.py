"""wang

re模块的运用
"""
import re
username = input("请输入用户名:")
qq = input("请输入QQ号:")

m1 = re.match(r"^[0-9a-zA-Z]{6,20}$",username)
if not m1:
    print("请输入有效的用户名")
m2 = re.fullmatch(r"[1-9]\d{4,11}",qq)
if not  m2:
    print("请输入有效的QQ号.")
if m1 and m2:
    print("你输入的信息是有效的")