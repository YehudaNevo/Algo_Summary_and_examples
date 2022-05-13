#            The Cigarette-Smokers Problem.

# Consider a system with three smoker processes and one agent process.
# Each smoker continuously rolls a cigarette and then smokes it. But to roll and smoke a cigarette,
# the smoker needs three ingredients: tobacco, paper, and matches. One of the smoker processes has paper,
# another has tobacco, and the third has matches. The agent has an infinite supply of all three materials.
# The agent places two of the ingredients on the table. The smoker who has the remaining ingredient
# then makes and smokes a cigarette, signaling the agent on completion. The agent then puts out another
# two of the three ingredients, and the cycle repeats. Write a pseudo code to synchronize the agent and
# the smokers. (hint: We use 5 semaphores. Semaphore smoker_tobacco, smoker_match, smoker_paper,
# agent are binary semaphores; and lock is used for mutual exclusion.)

#  SOLUTION
# Algo - three smokers make cigarette and try to consume it, if they cant make a cigarette - they go to sleep.
# the supplier process provide any of 2 ingredients and wake the proper smoker and go to sleep
#
import random
import threading
import time
from threading import *

#  ---   init the semaphores  -------
mutex = Semaphore(1)  # for mutual exclusion
agent = Semaphore(0)  # to check if the agent is free or busy
tobacco = Semaphore(0)
paper = Semaphore(0)
matches = Semaphore(0)


def agent_process():
    while True:
        mutex.acquire()
        select_item = random.randint(1, 3)

        if select_item == 1:
            matches.release()
        elif select_item == 2:
            paper.release()
        else:
            tobacco.release()

        mutex.release()
        agent.acquire()  # wll wake up only after one of the smokers finish to smoke and wake him


# the same for each one of them ...
def t_process():
    while True:
        tobacco.acquire()  # wake up only when the agent wake him
        mutex.acquire()  # release only after agent choose one and exit the critical section
        print("t  smoking")
        time.sleep(1)
        agent.release()  # can we switch the order here ?  - yes
        mutex.release()


def p_process():
    while True:
        paper.acquire()
        mutex.acquire()
        print("p  smoking")
        time.sleep(1)
        agent.release()
        mutex.release()


def m_process():
    while True:
        matches.acquire()
        mutex.acquire()
        print("m  smoking")
        time.sleep(1)
        agent.release()
        mutex.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=agent_process)
    t2 = threading.Thread(target=t_process)
    t3 = threading.Thread(target=p_process)
    t4 = threading.Thread(target=m_process)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
