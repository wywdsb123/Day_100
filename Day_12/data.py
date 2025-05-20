"""wang

数据的统计
"""
def ptp(data):
    return max(data)-min(data)
def mean(data):
    return sum(data) / len(data)
def median(data):
    temp,size=sorted(data),len(data)
    if size % 2 !=0:
        return temp[size//2]
    else:
        return mean(temp[size//2-1:size//2 +1])
def var(data ,ddof=1):
    x_bar = mean(data)
    temp = [(num -x_bar)**2 for num in data]
    return sum(temp)/(len(temp)-ddof)

def std(data,ddof =1):
    return var(data,ddof)**0.5

def cv(data,ddof=1):
    return std(data,ddof) / mean(data)

def describe(data):
    """输出描述性文字"""
    print(f"均值：{mean(data)}")
    print(f"中位数：{median(data)}")
    print(f"极差：{ptp(data)}")
    print(f"方差：{var(data):.3f}")
    print(f"标准差：{std(data):.3f}")
    print(f"变异系数：{cv(data):.3f}")
data = [10, 12, 23, 16]
describe(data)

