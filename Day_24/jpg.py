"""wang

谁懂期末周的无力感,加油吧
"""
from PIL import Image

image = Image.open("guido.jpg")

print(image.format)
print(image.size)
print(image.mode)
#image.show()"显示完整内容"
# 通过Image对象的crop方法指定剪裁区域剪裁图像
#image.crop((80, 20, 310, 360)).show()
# 通过Image对象的thumbnail方法生成指定尺寸的缩略图
image.thumbnail((128,128))
image.show()