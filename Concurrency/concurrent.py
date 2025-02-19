import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    name = input("Hey, enter your name: ")
    print(f"Hello, Mr. {name}")
    print(f"ask user time:  {time.time() - start}")

def complex_calc():
    print("started processing....")
    start = time.time()
    [x**2 for x in range(2100000)]
    print(f"complex calc time: {time.time() - start}")


# start = time.time()
# ask_user()
# complex_calc()
# print(f"total time: {time.time() - start}")

thread1 = Thread(target=ask_user)
thread2 = Thread(target=complex_calc)



start = time.time()
# thread1.start()
# thread2.start()
#
# thread1.join()   #we'll ask the main thread ot wait for the thread ot execute
# thread2.join()

with ThreadPoolExecutor as pool:
    pool.submit(ask_user)
    pool.submit(complex_calc)

print(f"total time: {time.time() - start}")
