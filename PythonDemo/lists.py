# my_arr = ["one", "two", "three", 3]
# print(my_arr)
# print(len(my_arr))


# friends = [["tom", 24], [24,"Sam"]]
# print(friends[0][0])
# friends.append(["david", 27])
# print(friends)
# friends.remove([24,"Sam"])
# print(friends)

# import gc

# list = ["Rolf", "Tom"]
# x_id = id(list)
# print(list, x_id)
# list.append("Sam")
# x_id = id(list)
# print(list, x_id)
# for obj in gc.get_objects():
#     if id(obj) == x_id: 
#         print("Found object:", obj)
#         break

list1 = (1,2,3)
list2 = (1,2,3)
x_id1 = id(list1)
x_id2 = id(list2)
# print(list1 is list2)
# print(list1)
# print(x_id1)
# print(list2)
# print(x_id2)

print(1 == True)

print(0.1 + 0.1 + 0.1 - 0.3)

a,b = 100, 100
print(a is b)
b,c = 1000,1000
print(b is c)

import gc
print(gc.get_count())
print(gc.get_stats())