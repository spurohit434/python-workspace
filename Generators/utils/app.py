#  generators are the function that remember the state of the function
# as we need large dataset now the problme here is the

def generate_hundreds():
    i = 0
    while i<100:
        yield i    # here the function remembers where it stopped last time
        i = i+1
        yield "This yeild stops it here"

gen_obj = generate_hundreds()
print(next(gen_obj))    # all methods like called as the iterators
# print(next(gen_obj))