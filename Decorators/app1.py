import functools

user = {'username': 'Jose', 'access_level': 'user'}

# decorator takes in a function and returns a function and that returned function must return the passed function

def third_level(access_level):
    def user_access(func):
        @functools.wraps(func)   #helps to get the function name
        def secure_func(args):   #this function is getting the args and passing the args to the function it is calling
            if user['access_level'] == access_level:
                return func(args)
        return secure_func
    return user_access

# @user_access
# def info():
#     return "user password is 1234\n"
#
# @user_access
# def trying_func():
#     return "hello admin\n"

@third_level('user')      # this decorator syntax makes the function calls for us
def info_panel(panel):
    return f"user password for {panel} is 1234\n"

# get_access = user_access(info)

# print(info())
print(info_panel('movies'))

# user_access = third_level('admin')
# info_panel = user_access(info_panel)


# print(trying_func.__name__) #both func give the same function name -> secure_func
# print(info.__name__)
