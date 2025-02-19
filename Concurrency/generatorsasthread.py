def counter(n):
    while n>=0:
        yield n   #the generators can also be used as the thread for yield the output as required
        n -= 1

# c1 = counter(20)
# c2 = counter(10)
#
# print(next(c1))
# print(next(c2))
# print(next(c1))
# print(next(c2))

tasks = [counter(20), counter(12)]
while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print("task finished")
