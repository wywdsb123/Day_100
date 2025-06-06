"""wang

替换字符串中的不良信息
"""
import re
sentence ="Oh.shit! 你是煞笔吗?Fuck you"
purified =re.sub("fuck|shit|[傻沙煞][比逼笔碧叉吊]",
                 "*",sentence,flags=re.IGNORECASE)
print(purified)