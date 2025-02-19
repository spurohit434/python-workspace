names  = []
for i in range(0,3):
    names.append(str(input(f"Enter your {i+1} friends name: ")))

friends_list = open('peoples.txt', 'r')
friends_names = [line.strip() for line in friends_list.readlines()]
friends_list.close()

names_set = set(names)
friends_names_set = set(friends_names)
print(names_set, friends_names_set)
common_names = names_set.intersection(friends_names_set)
print(f"Common friends are {common_names}")

nearby_file = open('nearby_friends.txt', 'w')
for name in common_names:
    nearby_file.write(f'{name}\n')
