import json

json_data = open('json_data.txt', 'r')
data = json.load(json_data)
json_data.close()
print(data[0]['id'])

#  syntax to open and close the files gracefully
with open('json_data.txt', 'r') as json_data:
    data = json.load(json_data)

# data1 = json.load(json_data) # this will give an error as we are trying to load the data after closing the file

