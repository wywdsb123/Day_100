"""wang

双色球进阶训练
"""
import random
RED_BALLS =[i for i in range(1,34)]
BLUE_BALLS = [i for i in range(1,17)]
def choose():
    selected_BALLS =random.sample(RED_BALLS,6)
    selected_BALLS.sort()
    selected_BALLS.append(random.choice(BLUE_BALLS))
    return selected_BALLS
def display(balls):
    for ball in balls[:-1]:
        print(f"\033[031m{ball:0>2d}\033[0m",end=" ")
    print(f"\033[034m{balls[-1]:0>2d}\033[0m")
n = int(input("生成几注号码："))
for _ in range(n):
    display(choose())