"""wang

学呗
"""
def select_sort (items, comp = lambda x,y:x<y ):
    items = items[:]
    for i in range(len(items)-1):
        min_index =i
        for j in range (i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items
        