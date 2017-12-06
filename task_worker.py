import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager
class QueueManager(BaseManager):
    """docstring for QueueManager"""
    pass

#犹豫这个QueueManager只从网络获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#链接到服务器，也就是运行 task_manager.py 的机器
server_addr = '127.0.0.1'
print('connect to server %s...'% server_addr)

#端口和验证码保持一致
m = QueueManager(address=(server_addr,5000),authkey=b'abc')

#从网络链接
m.connect()

#获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列取出任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...'% (n,n))
        r = '%d * %d = %d' %(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is Empty')

#处理结束
print('worker exit')
