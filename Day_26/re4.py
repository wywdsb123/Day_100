"""wang

拆分长字符串
"""
import re
poem ='窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r"[。,.，]",poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for index,sentence in enumerate(sentences_list):
 if (index+1)%2 !=0:
    print(sentence+",")
 else:
     print(sentence+".")