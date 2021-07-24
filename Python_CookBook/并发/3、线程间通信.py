from queue import Queue
from threading import Thread


def producer(out_q):
    while True:
        out_q.put()


def consumer(in_q):
    while True:
        data = in_q.get()


q = Queue
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
