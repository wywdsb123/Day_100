"""wang

不想学了,我去吃饭了,拜拜
"""
"""简单选择排序"""
def select_sort(items,comp = lambda x,y:x<y):
    items = items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items[min_index],items[i]

    return items
"""冒泡选择排序"""
def bubble_sort(items, comp = lambda x,y:x<y):
    items = items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j]
                swapped =True
        if not swapped:
            break
    return items
"""搅拌排序(冒泡排序升级版)"""
def bubble_sort(items,comp = lambda x,y:x>y):
    items = items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] =items[j+1][j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items)-2-i,i, -1):
                if comp(items[j-1],items[j]):
                    items[j],items[j-1] = i

