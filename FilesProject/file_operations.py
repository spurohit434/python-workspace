def save_to_file(data, filename):
    with open(filename, 'r') as file:
        file.write(data)


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()