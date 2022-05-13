import json
import urllib.request
import time
from threading import Thread, Lock, Condition

COUNTER = 0


def count_letters(url, frequency, mutex):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    mutex.acquire()
    for let in txt:
        letter = let.lower()
        if letter in frequency:
            frequency[letter] += 1
    global COUNTER
    COUNTER += 1
    mutex.release()


def main():
    # in that example we have share memory and sometime the result arnt correct
    frequency = {}
    mutex_cond = Condition()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(1000, 1020):
        Thread(target=count_letters,
               args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex_cond)).start()
    while (COUNTER < 20):
        time.sleep(1)

    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done time = ",
          end - start)  # if in one process usually about 50 sec , when we separated - 7 sec , with mutex_cond 8


main()
