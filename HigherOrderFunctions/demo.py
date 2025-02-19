def function(func):
    print("before")
    func()
    print("after")

def greet():
    print("hello world")


function(greet)