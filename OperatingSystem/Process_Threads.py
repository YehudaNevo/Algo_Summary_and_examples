import time
from multiprocessing import Process

from threading import Thread,Lock
import multiprocessing







#  GIL // in python its only improve tasks when its IO task .. not CPU  ( only in python ! )


#  Threads 1
# share memory, no isolation lighter only one cpu (in python)

# def do_work():
#     print("starting work")
#     count = 0
#     for i in range(1000000):
#         count += 1
#     print("finish work")


# because GIL we use only one cpu   - time shearing
# for _ in range(5):
#     t = Thread(target=do_work, args=())
#     t.start()

# process 2 now wll using all the cpus
# if __name__ == '__main__':
#     multiprocessing.set_start_method("spawn")
#     for _ in range(5):
#         p = Process(target=do_work, args=())
#         p.start()


# inter threads communication SHARE MEMORY








# def f(name):
#     print('hello', name)
#
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
#
#
# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=("yehuda",))
#     p.start()
#     p.join()

# class myThreead(threading.Thread):
#     def __init__(self, threadID, name, count):
#         threading.Thread.__init__(self)
#         self.id = threadID
#         self.name = name
#         self.count = count
#
#     def run(self):
#         print("starting " + self.name + "\n")
#
#         print_time(self.name, 1, self.count)
#         print("exit " + self.name)
#
#
# def print_time(name, delay, count):
#     while count:
#         time.sleep(delay)
#         print("%s: %s %s" % (name, time.ctime(time.time()), count))
#         count -= 1


# t1 = myThreead(1, "t1", 10)
# t2 = myThreead(1, "t2", 5)
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Done")

# in that example if wll delete the lock wll get unknown result
#
# def increment():
#     global x
#     x += 1
#
#
# def thread_task(lock):
#     for _ in range(100000):
#         lock.acquire()
#         increment()
#         lock.release()
#
#
# #
# def main_task():
#     global x  #
#     lock = threading.Lock()
#     x = 0  #
#     t1 = threading.Thread(target=thread_task(lock))
#     t2 = threading.Thread(target=thread_task(lock))
#     t1.start()
#     t2.start()
#
#
# for i in range(10):
#     main_task()
#     print("Iteration {0}: x = {1}".format(i, x))

# ---------------------------------------------------------------
