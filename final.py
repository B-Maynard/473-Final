import csv

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
	content_rating = 0
	budget = 0
	year = 0
	rating = 0
	totalFacebookLikes = 0
	

with open('movie_metadata.csv', 'rb') as csvfile:
    moviereader = csv.DictReader(csvfile)
    movies = MovieInfomation()
    for row in moviereader:
    	movies.name = row['movie_title']
    	movies.director = row['director_name']
    	movies.directorFacebookLikes = row['director_facebook_likes']
    	movies.duration = row['duration']
    	movies.leadActor = row['actor_1_name']
 		movies.leadActorFacebookLikes = row['actor_1_facebook_likes']
 		movies.gross = row['gross']
 		movies.genres = row['']
