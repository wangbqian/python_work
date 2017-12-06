"""从排好序的数组里面，删除重复的元素.重复的数字最多只能出现2次
nums=[1,1,1,2,2,5] 
要求返回nums=[1,1,2,2,3]"""



from collections import Counter
nums=[1,1,1,2,2,2,5,6,7,7,7] 

def saveDoubleNum(numbers):
    print Counter(numbers)
    for k, v in Counter(numbers).item():
        if v>2:
            numbers.removeNum(k)

    print numbers


saveDoubleNum(nums)