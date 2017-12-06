"""1.比如自然数10以下能被3或者5整除的有,3,5,6和9，那么这些数字的和为23.
求能被3或者5整除的1000以内数字的和"""

# sum = 0
# for i in range(1000):
#     if i % 3 == 0:
#         sum+=i
#     elif i%5 == 0:
#         sum+=i
print(sum(i for i in range(1000)if i%3 == 0 or i%5 == 0))