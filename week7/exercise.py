import threading, time
import random
from queue import Queue


class Box(object):

    lock = threading.RLock()

    def __init__(self):
        self.total_items = Queue()

    def add(self, n):
        Box.lock.acquire()
        self.total_items.put(n)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        if self.total_items.qsize() != 0:
            yield self.total_items.get()
        Box.lock.release()


def producer(box, items):
    while items > 0:
        item = random.randint(0, 256)
        print("adding item {0} in the box\n".format(item))
        box.add(item)
        time.sleep(5)
        items -= 1


def consumer(box, items):
    while items > 0:
        item_gen = box.remove()
        for item in item_gen:
            print("removing item {0} in the box\n".format(item))
        time.sleep(5)
        items -= 1


if __name__ == '__main__':
    items = 5
    print("putting {0} items in the box\n".format(items))
    box = Box()
    t1 = threading.Thread(target=producer, args=(box, items))
    t2 = threading.Thread(target=consumer, args=(box, items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("{0} items still remain in the box".format(box.total_items.qsize()))
