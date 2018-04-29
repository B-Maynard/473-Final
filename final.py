import csv

with open('movie_metadata.csv', 'rb') as csvfile:
    moviereader = csv.reader(csvfile, delimiter=',')
    for row in moviereader:
        print row
