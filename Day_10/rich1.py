"""王

常用结构之列表2
"""
import random
from rich.console import Console
from rich.table import Table

console =Console()
n = int(input("请输入数量："))
red_balls=[i for i  in range(1,34)]
blue_balls=[i for i in range(1,17)]
table=Table(show_header=True)
for col_name in ("序号","红球","蓝球"):
    table.add_column(col_name,justify="center")
for i in range(n):
    select_ball=random.sample(red_balls,6)
    select_ball.sort()
    blue1 = random.choice(blue_balls)
    table.add_row(
        str(i+1),
        f"[red]{" ".join([f"{ball:0>2d}"for ball in select_ball])}[/red]",
        f"[blue]{blue1:0>2d}[/blue]"
    )
console.print(table)
