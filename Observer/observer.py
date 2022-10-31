"""
In this pattern, objects are represented as observers that wait for an event to trigger. 
An observer attaches to the subject once the specified event occurs. 
As the event occurs, the subject tells the observers that it has occurred.

"""

import threading
import time
import pdb


class Downloader(threading.Thread):
    def run(self):
        print("downloading")
        for i in range(1, 5):
            self.i = i
            time.sleep(2)
            print("unfunf")
            return "hello world"


class Worker(threading.Thread):
    def run(self):
        for i in range(1, 5):
            print("worker running: %i (%i)" % (i, t.i))
            time.sleep(1)
            t.join()

            print("done")


t = Downloader()
t.start()

time.sleep(1)

t1 = Worker()
t1.start()

t2 = Worker()
t2.start()

t3 = Worker()
t3.start()
