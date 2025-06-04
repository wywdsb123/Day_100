"""wang

有趣的感觉
"""

from PIL import Image
image = Image.open('xuge.png')
# 使用Image对象的rotate方法实现图像的旋转
image.rotate(45).show()
# 使用Image对象的transpose方法实现图像翻转
# Image.FLIP_LEFT_RIGHT - 水平翻转
# Image.FLIP_TOP_BOTTOM - 垂直翻转
#image.transpose(Image.FLIP_TOP_BOTTOM).show()
# for x in range(80, 310):
#     for y in range(20, 360):
#         # 通过Image对象的putpixel方法修改图像指定像素点
#         image.putpixel((x, y), (128, 128, 128))
# image.show()
from PIL import ImageFilter

# 使用Image对象的filter方法对图像进行滤镜处理
# ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
image.filter(ImageFilter.CONTOUR).show()
