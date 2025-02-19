from copy import deepcopy

l1 = [12,33,4,1,12]
l2 = []
l2.extend(l1)
l3 = [l1]   # appends by default

print(id(l1), l1)
print(id(l2), l2)
print(id(l3), l3)

