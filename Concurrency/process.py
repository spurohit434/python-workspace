import time
from multiprocessing import Process

def complex_calc():
    print("started processing....")
    start = time.time()
    [x**2 for x in range(2100000)]
    print(f"complex calc time: {time.time() - start}")


start = time.time()
process2 = Process(target=complex_calc)

print(f"total time: {time.time() - start}")

if __name__ == '__main__':
    process2.start()
