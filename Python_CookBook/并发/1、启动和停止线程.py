"""
并发
"""
import multiprocessing
import socket
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
# 查询线程是否在运行
if t.is_alive():
    print('Still running')
else:
    print('Completed')


# 对于长时间运行的线程或者一直不断运行的后台任务，应该考虑将这些线程设置为daemon(守护线程)


# 终止线程、给线程发信号、调整线程调度属性以及执行任何其他的高级操作
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
# 主线程运行函数
c.terminate()
t.join()


# 为线程加上超时循环
class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):  # sock is a socket
        sock.settimeout(5)  # set timeout period
        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # continued processing
        # terminated
        return


# 继承线程类
class CountdownThread(Thread):
    def __init__(self):
        super().__init__()
        self.n = 0

    def run(self, n):
        while self.n >= 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


c = CountdownTask(5)
c.start()

# 多进程
c = CountdownTask(5)
p = multiprocessing.Process(target=c.run)
p.start()

