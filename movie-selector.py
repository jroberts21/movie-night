import csv

def print_movies(movies):
    for row in movies:
        print(row['title'])
        
        
with open('movie-list.csv') as f:
    movies = csv.DictReader(f)
    print_movies(movies)