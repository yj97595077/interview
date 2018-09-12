#!/usr/bin/python

import sys
import time
from threading import Thread
import Queue

q = Queue.Queue()

class WorkerThread(Thread):
    def __init__(self):
        super(WorkerThread, self).__init__()

    def run(self):
        while True:
            args = q.get()
            a = args[0]
            b = args[1]
            c = a + b
            print '%s + %s = %s' % (a, b, c)
            q.task_done()
            time.sleep(5)

class ThreadPool(object):
    def __init__(self, pool_num=5):
        self.pool_num = pool_num

    def init_pool(self):
        for index in range(self.pool_num):
            thread = WorkerThread()
            thread.setDaemon(True)
            thread.start()

    def add_task(self, a, b):
        args = [a, b]
        q.put(args)

thread_pool = ThreadPool()
thread_pool.init_pool()
for i in range(5):
    for j in range(40,45):
        thread_pool.add_task(i, j)

q.join()

