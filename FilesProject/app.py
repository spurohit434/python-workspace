my_file = open('data.txt', 'r')
file_data = my_file.read()
my_file.close()
print(file_data)

my_file_write = open('data.txt', 'w')      # used to write the text in the file and used to override
my_file_write.write("to the matrix")
# my_file = my_file_write.read()
print(my_file)