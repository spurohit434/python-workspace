from typing import List

my_numbers = [1,2,3,4,5]
add_1 = lambda x,y: x+1+y

print(list(map(lambda x:x+1, my_numbers )))

print(add_1(my_numbers[1],my_numbers[2]))
b = -0.0
print(bool(b))