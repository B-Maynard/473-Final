import csv
from more_itertools import unique_everseen

# Reads csv file and takes into account the first row as the headers for the columns

class MovieInfomation():
	name = ""
	director = ""
	directorFacebookLikes = 0
	duration = 0
	leadActor = ""
	leadActorFacebookLikes = 0
	gross = 0
	genres = ""
	voterNumber = 0
	contentRating = 0
	budget = 0
	year = 0
	rating = 0
	totalFacebookLikes = 0


with open('movie_metadata.csv', 'r') as csvfile, open('2.csv', 'w') as out_file:
    # TODO: 2.csv has to be opened to be read in order to be manipulated on line 28
    out_file.writelines(unique_everseen(csvfile))
    moviereader = csv.DictReader(out_file)
    movies = MovieInfomation()
    for row in moviereader:
    	movies.name = row['movie_title']
    	movies.director = row['director_name']
    	movies.directorFacebookLikes = row['director_facebook_likes']
    	movies.duration = row['duration']
    	movies.leadActor = row['actor_1_name']
        movies.leadActorFacebookLikes = row['actor_1_facebook_likes']
        movies.gross = row['gross']
        movies.genres = row['genres']
        movies.voterNumber = row['num_voted_users']
        movies.contentRating = row['content_rating']
        movies.budget = row['budget']
        movies.year = row['title_year']
        movies.rating = row['imdb_score']
        movies.totalFacebookLikes = row['movie_facebook_likes']
