import multiprocessing
import time

def cpu_task(n):
    """Simulates a CPU-intensive task by calculating squares."""
    print(f"Process {multiprocessing.current_process().name} processing...")
    sum([i**2 for i in range(n)])

N = 10**7  # Large number for CPU workload

processes = []
start_time = time.time()

for _ in range(4):  # Creating 4 processes
    p = multiprocessing.Process(target=cpu_task, args=(N,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

end_time = time.time()
print(f"Multiprocessing Execution Time: {end_time - start_time:.2f} seconds")
