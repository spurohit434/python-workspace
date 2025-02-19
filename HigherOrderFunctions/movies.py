movies = [
    {'name': 'Dictator', 'director':'Fronsky'},
    {'name': 'Adaptor', 'director':'Joskey'},
    {'name': 'Comentator', 'director':'Consky'},
    {'name': 'Tutor', 'director':'Crewsky'},
    {'name': 'Developer', 'director':'Bisky'},
    {'name': 'Shaava', 'director':'Whisky'},
]

find_by = input("enter the field {name or director} by which you are searching the movie?: ")
field_value = input(f"enter the value of the {find_by} here: ")

def find_movie(finder):
    for movie in movies:
        print(finder(movie))

find_movie(lambda movie: movie[find_by])