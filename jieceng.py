def factorial(num, cache={}):
    if num == 0:
        return 1
    if num not in cache:
        print(num)
        cache[num] = factorial(num - 1) * num
        print('jieceng',num)
    return cache[num]

print(factorial(10))
print("-------")
print(factorial(3))

