"""wang

filter , map , sorted
"""
def is_even(num):
    return num%2==0
def square(num):
    return num**2

old_nums =[35,12,34,56]
new_nums=list(map(square,filter(is_even,old_nums)))
#filter 过滤数据 map 映射数据
print(new_nums)
# old_nums = [35, 12, 8, 99, 60, 52]
# new_nums = [num ** 2 for num in old_nums if num % 2 == 0]
# print(new_nums)  # [144, 64, 3600, 2704]

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key=len)
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']