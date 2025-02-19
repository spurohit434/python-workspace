 # all the objects having the __next__ method are iterators

class hundreds_generators:
    def __init__(self):
        self.number = 0

    def __next__(self):    # all the classes having this are the iterators
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()



# generators = hundreds_generators()
# generators.__next__()
# print(next(generators))


# class five_iterator:
#     def __init__(self):
#         self.numbers = [1,2,3,4,5]
#         self.iterator = 0
#
#     def __next__(self):
#         if self.iterator < len(self.numbers):
#             current = self.numbers[self.iterator]
#             self.iterator += 1
#             return current
#         else:
#             raise StopIteration()
#
#
# iterator = five_iterator()
# # iterator.__next__()
# print(next(iterator))



class five_hundred_iterator:     #this is my iterable as it is having th iter method in it

    def __iter__(self):
        obj = hundreds_generators()
        print(next(obj))
        return obj

print(sum(five_hundred_iterator()))


# list comprehension
obj = [x for x in [1,2,3,4,5]]
print((obj))

# generator comprehension
obj = (x for x in [1,2,3,4,5])
print(next(obj))  # return an yield value from the list






