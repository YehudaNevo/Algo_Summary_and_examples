import multiprocessing
import time
from multiprocessing import Process


def print_array(arr):
    while True:
        print(*arr, sep=", ")
        time.sleep(1)


if __name__ == "__main__":

    arr = multiprocessing.Array("i", [-1] * 10,lock=True)
    p = Process(target=print_array, args=([arr]))
    p.start()
    for j in range(10):
        time.sleep(1)
        for i in range(10):
            arr[i] = j
