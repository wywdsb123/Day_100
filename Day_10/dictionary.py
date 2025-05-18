"""王

常用数据结构之字典
"""
# # dict函数(构造器)中的每一组参数就是字典中的一组键值对
# person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
# print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
#
# # 可以通过Python内置函数zip压缩两个序列并创建字典
# items1 = dict(zip('ABCDE', '12345'))
# print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
# items2 = dict(zip('ABCDE', range(1, 10)))
# print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
#
# # 用字典生成式语法创建字典
# items3 = {x: x ** 3 for x in range(1, 6)}
# print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
# person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
#
# # 成员运算
# print('name' in person)  # True
# print('tel' in person)   # False
#
# # 索引运算
# print(person['name'])
# print(person['addr'])
# person['age'] = 25
# person['height'] = 178
# person['tel'] = '13122334455'
# person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
# print(person)
#
# # 循环遍历
# for key in person:
#     print(f"{key}:\t{person[key]}")
sentence =input("说话")
counter = {}
for ch in sentence:
    if "A"<=ch<="Z"or "a"<=ch<="z":
        counter[ch]=counter.get(ch,0)+1
sorted_counter = sorted(counter,key=counter.get,reverse=True)
for key in sorted_counter:
    print(f"{key}出现了{counter[key]}次")
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)