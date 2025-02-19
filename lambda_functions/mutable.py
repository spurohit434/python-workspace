friends_dict = { "Rolf" : "31", "Name" : "Suneel"}

print(id(friends_dict))

def see_friends_list(friends, name):
    print(id(friends))
    print(id(friends["Rolf"]))

print(id(friends_dict))

see_friends_list(friends_dict, "Rolf")