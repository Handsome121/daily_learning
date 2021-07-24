"""
我们想要实现一个队列，它能够以给定的优先级来对元素排序，且每次pop操作时都会返回优先级最高的那个元素。
学习堆的相关知识
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('bar'), 6)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q._queue)
print(q.pop())
