"""从排序好的任意数组列表里面删除重复元素(你不知道列表里面有多少个重逢的元素)
比如:nums=[1,3,3,5,5,8,10,10,100,100],处理完之后是:[1, 3, 5, 8, 10, 100]"""

def noMult(n_list):
    n_set = set(n_list)
    n_list = list(n_set)
    return sorted(n_list)

numsL = [1,3,3,5,5,8,10,10,100,100]
# numsS = set(numsL)
# numsL  = list(numsS)

print(noMult(numsL))



print(sorted(set(numsL)))