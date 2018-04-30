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
	contentRating = 0
	budget = 0
	year = 0
	rating = 0
	totalFacebookLikes = 0
	def printMovieInfo(self):
		return self.name
	

with open('movie_metadata.csv', 'rb') as csvfile:
	moviereader = csv.DictReader(csvfile)
	currentMovie = MovieInfomation()
	currentMovie.director = "Logan"
	movies = []
	#get currentMovie number 
	for row in moviereader:
		pass
	movieLen = moviereader.line_num
	print movieLen
	csvfile.seek(0)
	#fills current then adds current to list 
	for row in moviereader:
		currentMovie.name = row['movie_title']
		currentMovie.director = row['director_name']
		currentMovie.directorFacebookLikes = row['director_facebook_likes']
		currentMovie.duration = row['duration']
		currentMovie.leadActor = row['actor_1_name']
		currentMovie.leadActorFacebookLikes = row['actor_1_facebook_likes']
		currentMovie.gross = row['gross']
		currentMovie.genres = row['genres']
		currentMovie.voterNumber = row['num_voted_users']
		currentMovie.contentRating = row['content_rating']
		currentMovie.budget = row['budget']
		currentMovie.year = row['title_year']
		currentMovie.rating = row['imdb_score']
		currentMovie.totalFacebookLikes = row['movie_facebook_likes']
		#print currentMovie.name
		movies.append(currentMovie) 