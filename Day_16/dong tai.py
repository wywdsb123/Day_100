"""wang

动态属性
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

stu = Student("wang",20)
stu.sex = '男'

