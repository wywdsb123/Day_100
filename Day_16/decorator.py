"""wang

可见性问题
"""
class Student:
    def __init__(self,name,age):
        self.__name =name
        self.__age = age

    def study(self,course_name):
        print(f"{self.__name}正在学习{course_name}")

stu = Student("wang",23)
stu.study("python")
print(stu.__dict__)#__name 开头的属性是私有的不对外开放 #__dict__就可以，不知道为啥

