import threading
import time

def cpu_task(n):
    """Simulates a CPU-intensive task by calculating squares."""
    print(f"Thread {threading.current_thread().name} processing...")
    sum([i**2 for i in range(n)])

N = 10**7  # Large number for CPU workload

threads = []
start_time = time.time()

for _ in range(4):  # Creating 4 threads
    t = threading.Thread(target=cpu_task, args=(N,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"Multithreading Execution Time: {end_time - start_time:.2f} seconds")
