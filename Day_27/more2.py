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
"""合并(将两个有序的列表合并成一个有序的列表)"""
def merge(items1,items2,comp=lambda x,y:x<y):
    items = []
    index1,index2 =0 , 0
    while index1 <len(items1) and index2<len(items2):
        if comp (items1[index1],items2[index2]):
            items.append(items1[index1])
            index1 +=1
        else:
            items.append(items2[index2])
            index2 +=1
    items += items1[index1:]
    items += items2[index2:]
    return items
def merge_sort (items,comp=lambda x,y:x<y ):
    return _merge_sort(list(items),comp)
def _merge_sort(items,comp):
    if len(items)<2:
        return items
    mid =len(items)//2
    left = _merge_sort(items[:mid],comp)
    right = _merge_sort(items[mid:],comp)
    return merge(left,right,comp)

"""顺序查找"""
def seq_search(items,key):
    for index,item  in enumerate(items):
        if item == key:
            return index
    return -1

"""折半查找"""
def bin_search(items,key):
    start ,end = 0,len(items)-1
    while start<=end :
        mid =(start +end )//2
        if key >items[mid]:
            start = mid +1
        elif key <items[mid]:
            end = mid -1
        else:
            return mid
    return -1






