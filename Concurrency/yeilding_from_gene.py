from collections import deque

friends = deque(("hello", "world", "from", "python", "&", "java"))

def get_values():
    yield from friends

# print(next(get_values()))

cnt  = 0
while cnt < len(friends):
    print(next(get_values()))
    cnt += 1