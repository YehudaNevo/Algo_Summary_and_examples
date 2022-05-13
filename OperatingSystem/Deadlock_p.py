import time
import threading

mutex1 = threading.Lock()
mutex2 = threading.Lock()

# sample example od deadlock with crossing the mutexes
def process_1(m1, m2):
    while True:
        print("p1 aq - 1")
        m1.acquire()
        print("p1 aq - 2")
        m2.acquire()
        time.sleep(0.2)
        m1.release()
        m2.release()
        print("p1 re - 1,2 ")

def process_2(m1, m2):
    while True:
        print("p2 aq - 2")
        m2.acquire()
        print("p2 aq - 1")
        m1.acquire()
        time.sleep(0.2)
        m1.release()
        m2.release()
        print("p2 re - 1,2 ")





if __name__ == "__main__":
    pass
    # t1 = threading.Thread(target=process_1, args=(mutex1, mutex2))
    # t2 = threading.Thread(target=process_2, args=(mutex1, mutex2))
    # t1.start()
    # t2.start()













