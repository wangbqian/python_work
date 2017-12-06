# def _odd_iter():
#     n = 1 
#     while True:
#         n = n + 2
#         yield n 

# def _not_divisible(n):
#     return lambda x:x % n > 0

# def prinmes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n 
#         it = filter(_not_divisible(n),it)

# for n in prinmes():
#     if n<1000:
#         print(n)
#     else:
#         break


# #filter筛选回数
# def is_palindrome(numbers):
#     return str(numbers)[::] == str(numbers)[::-1] and numbers>10

# output = filter(is_palindrome, range(1, 1000))
# print(list(output))

#普通函数筛选回数
def is_palindrome2(n):
    if str(n)==str(n)[::-1] and n >10:
        return n 
num = [x for x in range(1,1000) if is_palindrome2(x)]
# if num is not None:
print(num)



