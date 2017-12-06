
from functools import wraps
# from time import time,sleep


# start_time = time()
# print('\n现在开始运行  \n\n**************************\n')


# def log(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapers(*args,**kw):
#             print('函数{0}()即将执行，此时系统已运行了{1} 秒\n'.format(func.__name__,time()-start_time))
#             startTime = time()
#             return (func(*args,**kw),print('函数{0}()执行了{1}秒后，结束了自己\n'.format(func.__name__,time()-startTime)))[0]
#         return wrapers
#     return (decorator,print('我是一个带参数的装饰器，我的参数是"{}"'.format(text)))[0] if text.__str__() == text else decorator(text)


# @log()
# def abc():
#     print('我是函数abc(),我正在执行中，不给过我要睡 5 秒\n')
#     sleep(5)

# @log('这里是下一个\n')
# def efg():
#     print('我是函数 efg()，我正在执行中，我想睡 3 秒\n')
#     sleep(3)


# abc()
# efg()

# print('运行结束，一共云心了',time() - start_time," 秒。")






# def log(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s():' % (text,func.__name__))
#             return (func(*args,**kw),print('end'))[0]
#         return (wrapper,print('begin'))[0]

#     return decorator

# @log('zheshi')
# def f():
#     return 'this'

# f()


#书上的例子
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log('execute')
# def now():
#     print('2015-3-25')


# now()