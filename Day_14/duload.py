"""wang

计时器功能
"""
import random
import time

def download(filename):
    """下载文件"""
    print(F"开始下载{filename}")
    time.sleep(random.random() *10)
    print(f"{filename}下载完成")
def upload(filename):
    """上传文件"""
    print(F"文件开始上传{filename}.")
    time.sleep(random.random()*8)
    print(f"{filename}上传完成")
start =time.time()
download("MySQL从删库到跑路.avi")
end = time.time()
print(f"花费时间：{end-start:.2f}秒")
start = time.time()
upload('Python从入门到住院.pdf')
end =time.time()
print(f"花费时间：{end-start:.2f}秒")
