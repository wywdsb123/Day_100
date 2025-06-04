"""wang

有趣的感觉
"""
from PIL import Image

xuge_image =Image.open("xuge.png")
guido_image =Image.open("guido.jpg")
guido_head =guido_image.crop((80,20,310,360))
width ,height =guido_head.size
xuge_image.paste(guido_head.resize((int(width/0.5),int(height/0.5))),(900,100))
xuge_image.show()