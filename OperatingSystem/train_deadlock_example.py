import time
import threading


class Train:
    def __init__(self, uid, length, front):
        self.uid = uid
        self.length = length
        self.front = front


class Intersections:
    def __init__(self, uid, mutex, lock_by):
        self.uid = uid
        self.mutex = mutex
        self.locked_by = lock_by


class Crossing:
    def __init__(self, position, intersections):
        self.position = position
        self.intersections = intersections


def train_move(train,dis,crossings):
    while train.front < dis:
        train.front += 1
        for crs in crossings:
            if train.front == crs.position:
                crs.intersection.mutex.aquire()
                crs.intersection.lock_by = train.uid
            back = train.front - train.length
            if back == crs.position:
                crs.intersection.lock_by = -1
                crs.intersection.mutex.release()

        time.sleep(0.01)


