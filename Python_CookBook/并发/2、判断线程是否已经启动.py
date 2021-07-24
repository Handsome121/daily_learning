"""
我们加载了一个线程，但是想知道它实际会在什么时候开始运行
"""
import threading
import time
from threading import Event, Thread


def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()  # 设置事件，所有等待事件设置的任务将立即被唤醒
    while n >= 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


started_evt = Event()  # 创建一个事件对象
print('launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()
started_evt.wait()  # 等待事件被设置，如果事件被设置，立即返回True,否则阻塞，直到另一个任务调用set()
print('countdown is running')


# --------Event()对象的关键特性就是它会唤醒所有等待的线程，如果我们只希望唤醒一个单独的线程，那么最好使用semaohore或者Condition对象

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


ptimer = PeriodicTimer(5)
ptimer.start()


def countdown(nicks):
    while nicks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nicks)
        nicks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1


threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()


# 使用信号量
def worker(n, sema):
    sema.acquire()
    print('Working', n)


sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()
print(sema.release())
print(sema.release())
print(sema.release())
# 每次释放信号量时，只有一个工作者线程会被唤醒并投入运行

