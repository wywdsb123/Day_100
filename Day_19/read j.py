"""wang

读取json中文件以python字典形式走出
"""
import json



with open('data.json' ,'r')as file:
    my_dict=json.load(file)
    print(type(my_dict))
    print(my_dict)