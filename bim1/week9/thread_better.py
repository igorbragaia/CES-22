# threads are better when you want share memory and
# multiprocessing is better when you dont wanna share memory

from pprint import pprint
import threading
import time


class Box(object):

    lock = threading.RLock()

    def __init__(self):
        self.total_items = []

    def add(self, n):
        Box.lock.acquire()
        self.total_items.append(n)
        Box.lock.release()


def producer(box, items):
    for item in range(5):
        box.add(item)
        time.sleep(5)
        items -= 1


if __name__ == '__main__':
    items = 5
    box = Box()
    t1 = threading.Thread(target=producer, args=(box, items))
    t2 = threading.Thread(target=producer, args=(box, items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pprint(box.total_items)
