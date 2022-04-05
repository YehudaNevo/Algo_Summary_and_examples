import threading
import os


# in that example if wll delete the lock wll get unknown result

def increment():
    global x
    x += 1


def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


#
def main_task():
    global x  #
    lock = threading.Lock()
    x = 0  #
    t1 = threading.Thread(target=thread_task(lock))
    t2 = threading.Thread(target=thread_task(lock))
    t1.start()
    t2.start()


for i in range(10):
    main_task()
    print("Iteration {0}: x = {1}".format(i, x))

# ---------------------------------------------------------------
