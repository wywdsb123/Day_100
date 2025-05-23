"""wang

设置了一个时钟
"""
import time

class Clock:
    def __init__(self,hour = 0,minute = 0,second=0):
        self.hour=hour
        self.minute=minute
        self.sec=second
    def run(self):
        self.sec+=1
        if self.sec==60:
            self.sec=0
            self.minute+=1
            if self.minute==60:
                self.minute=0
                self.hour+=1
                if self.hour==24:
                    self.hour=0
    def show(self):
        """显示时间"""
        return f"{self.hour:0>2d}:{self.minute:0>2d}:{self.sec:0>2d}"

    def clear_screen(self):
        """通用清屏方法（不依赖os.system）"""
        print("\033[H\033[J", end="")  # ANSI转义序列[6](@ref)

clock =Clock(23,59,58)

while True:
    clock.clear_screen()
    print(clock.show())
    time.sleep(1)
    clock.run()
