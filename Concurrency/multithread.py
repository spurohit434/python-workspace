import random
from threading import Thread
import time
import queue
from traceback import print_tb

counter = 0
job_queue = queue.Queue()  #thing to be printed out
cnt_queue = queue.Queue()  #thing to increment the coutner by

def inc_counter():
    global counter
    while True:
        increment = cnt_queue.get()
        old_counter = counter
        new_counter = old_counter + increment
        job_queue.put((f" new counter is: {new_counter}"))
        cnt_queue.task_done()
    # global counter
    # time.sleep(random.random())
    # counter += 1
    # time.sleep(random.random())
    # print("-------")
    # print(f"Value of counter is {counter}")
    # print("-------")
    # time.sleep(random.random())

for x in range(10):
    t1 = Thread(target = inc_counter, daemon=True)
    # time.sleep(random.random())
    t1.start()
    # inc_counter()

def print_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target=print_manager, daemon=True).start()

def increment_counter():
    cnt_queue.put(1)

Thread(target=increment_counter(), daemon=True).start()

