"""在一个数组指定数组里面移除指定的数字,并返回新的数组并从大到小排序
比如:nums=[1,6,6,3,6,2,10,2,100],remove_num=6
要求返回时nums=[1, 2, 3, 10, 100]"""



# def removeNum(numbers,number):
#     lenNum = len(numbers)
#     for i in range(lenNum):
#         if numbers[i] == number:
#             numbers.remove(number)
#             newNums = numbers.remove(number)
#             removeNum(newNums,number)
    # return numbers
    

def removeNum(numbers,number):
    numCount = numbers.count(number)
    for i in range(numCount):
        numbers.remove(number)
        # numbers.sort()
    return sorted(numbers)
nums=[1,6,6,3,6,2,10,2,100]
remove_num = 6
nums = removeNum(nums,remove_num)
print(nums)