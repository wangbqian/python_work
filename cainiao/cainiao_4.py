"""从排好序的数组里面，删除重复的元素.重复的数字最多只能出现2次
nums=[1,1,1,2,2,5] 
要求返回nums=[1,1,2,2,5]"""



from collections import Counter
nums=[1,1,1,2,2,2,5,6,7,7,7] 

def saveDoubleNum(numbers):
    c = Counter(numbers)
    for k, v in c.items():
        if v>2:
            numbers.remove(k)

    print(numbers)


saveDoubleNum(nums)