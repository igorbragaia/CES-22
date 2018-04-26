# threads are better when you want share memory and
# multiprocessing is better when you dont wanna share memory

import multiprocessing
import time
from pprint import pprint


class Items(multiprocessing.Process):

    def run(self):
        total_items = []
        for item in range(5):
            total_items.append(item)
            time.sleep(5)
        pprint(total_items)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Items()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
