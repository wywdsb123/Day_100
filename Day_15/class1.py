"""wang

类的初步掌握
"""
class Student:
    def study(self,course_name):
        print(f"学生正在学习{course_name}")
    def play(self):
        print(f"学生正在玩游戏")
stu1=Student()
stu2=Student()
print(stu1)
print(stu2)
print(hex(id(stu1)),hex(id(stu2)))
# 通过“类.方法”调用方法
# 第一个参数是接收消息的对象
# 第二个参数是学习的课程名称
Student.study(stu1,"Python程序设计")
# 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法
# 点前面的对象就是接收消息的对象

stu1.study("Python 程序设计")
Student.play(stu2)
stu2.play()
# 只需要传入第二个参数课程名称
                    # 学生正在玩游戏.