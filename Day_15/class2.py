"""wang

类的练习
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age=age

    def study(self,course_name):
        print(f"{self.name} is studing{course_name}.")

    def play(self):
        print(f"{self.name} is playing.")
stu1 = Student("wang",44)
stu2 = Student("lei",23)
stu1.study('python')
stu2.play()