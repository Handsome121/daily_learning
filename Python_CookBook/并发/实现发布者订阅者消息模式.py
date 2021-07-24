"""
我们要解决一个基于多线程通信间的问题，希望实现发布者订阅者模式
"""
from collections import defaultdict


class Exchagnge:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


_exchanges = defaultdict(Exchagnge)


def get_exchange(name):
    return _exchanges[name]


class Task:
    def send(self, msg):
        pass


task_a = Task()
task_b = Task()
exc = get_exchange('name')
exc.attach(task_a)
exc.attach(task_b)
exc.send('msg1')
exc.send('msg2')
exc.detach(task_a)
exc.detach(task_b)

