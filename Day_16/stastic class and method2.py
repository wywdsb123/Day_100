"""wang

静态与类方法
"""
class Triangle(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    @staticmethod
    def is_valid(cls,a,b,c):
        return a+b>c and a+c>b and b+c>a
    @property
    def perimeter(self):
        return self.a +self.b +self.c
    @property
    def area(self):
        p = self.perimeter/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
t= Triangle(3,4,5)
print(f"周长；{t.perimeter}")
print(f"面积：{t.area}")