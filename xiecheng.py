import inspect

def simple_coroutine(a):
    print(' - > coroutine started: a = ',a)
    b = yield a 
    print(' - > Received: b = ' ,b)
    c = yield a + b
    print('- > Received v = ' ,c)



my_coro2 = simple_coroutine(14)
print(inspect.getgeneratorstate(my_coro2))


next(my_coro2)


print(inspect.getgeneratorstate(my_coro2))


my_coro2.send(28)
next(my_coro2)

print(inspect.getgeneratorstate(my_coro2))

my_coro2.send(99)
