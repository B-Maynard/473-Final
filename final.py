import csv
from ggplot import *
import pandas as pd
########################Import data ########################

#create a dataframe of movies and fill data from csv file
df = pd.read_csv('movie_metadata.csv')

##########################Remove Unneeded data #############
#Remove unneeded values 
df = df.drop(
	columns=['color', 'actor_3_name', 
	'actor_3_facebook_likes', 'facenumber_in_poster', 
	'plot_keywords', 'movie_imdb_link','aspect_ratio']
)

#get rows num before duplicate deletion
beforeDel = len(df)
df = df.drop_duplicates()
print str(beforeDel - len(df)) + " Duplicate records removed"

#Print values about remaining data 
rows = len(df)
cols = len(df.columns)
print str(len(df)) + " rows \t" + str(len(df.columns)) + " columns\n"

##########################Cleaning #########################

#print extensive view of missing values 
#print df.isnull().sum().to_string() + "\n"

#clean whitespace of movie titles 
df['movie_title'] = df['movie_title'].str.strip()

#fill missing duration value with the mean
df['duration'] = df['duration'].fillna(df['duration'].mean().round())

#fill mising countries with a space
df['country'] = df['country'].fillna('') 

##########################Visualisation#####################

#Plots

# yearHist = ggplot(df, aes(x="title_year")) +\
# ggtitle("Movie data by year") + xlab("Year") + ylab("Amount") +\
# geom_histogram(binwidth=.05)

# print yearHist
# yearHist.save('yearHist.png')
genreDfs = []

actionDf = df[df['genres'].str.contains("Action")]
adventureDf = df[df['genres'].str.contains("Adventure")]
animationDf = df[df['genres'].str.contains("Animation")]
biographyDf = df[df['genres'].str.contains("Biography")]
comedyDf = df[df['genres'].str.contains("Comedy")]
crimeDf = df[df['genres'].str.contains("Crime")]
documentaryDf = df[df['genres'].str.contains("Documentary")]
dramaDf = df[df['genres'].str.contains("Drama")]
familyDf = df[df['genres'].str.contains("Family")]
fantasyDf = df[df['genres'].str.contains("Fantasy")]
filmNoirDf = df[df['genres'].str.contains("Film-Noir")]
historyDf = df[df['genres'].str.contains("History")]
horrorDf = df[df['genres'].str.contains("Horror")]
musicalDf = df[df['genres'].str.contains("Musical")]
mysteryDf = df[df['genres'].str.contains("Mystery")]
newsDf = df[df['genres'].str.contains("News")]
romanceDf = df[df['genres'].str.contains("Romance")]
sciFiDf = df[df['genres'].str.contains("Sci-Fi")]
shortDf = df[df['genres'].str.contains("Short")]
sportDf = df[df['genres'].str.contains("Sport")]
thrillerDf = df[df['genres'].str.contains("Thriller")]
warDf = df[df['genres'].str.contains("War")]
westernDf = df[df['genres'].str.contains("Western")]
genres = [
["Action", actionDf.imdb_score.mean().round(2)],
["Adventure", adventureDf.imdb_score.mean().round(2)],
["Animation", animationDf.imdb_score.mean().round(2)],
["Biography", biographyDf.imdb_score.mean().round(2)],
["Comedy", comedyDf.imdb_score.mean().round(2)],
["Crime", crimeDf.imdb_score.mean().round(2)],
["Documentary", documentaryDf.imdb_score.mean().round(2)],
["Drama", dramaDf.imdb_score.mean().round(2)],
["Family", familyDf.imdb_score.mean().round(2)],
["Fantasy", fantasyDf.imdb_score.mean().round(2)], 
["Film-Noir", filmNoirDf.imdb_score.mean().round(2)],
["History", historyDf.imdb_score.mean().round(2)],
["Horror", horrorDf.imdb_score.mean().round(2)],
["Musical", musicalDf.imdb_score.mean().round(2)],
["Mystery", mysteryDf.imdb_score.mean().round(2)],
["News", newsDf.imdb_score.mean().round(2)],
["Romance", romanceDf.imdb_score.mean().round(2)],
["Sci-Fi", sciFiDf.imdb_score.mean().round(2)],
["Short", shortDf.imdb_score.mean().round(2)],
["Sport", sportDf.imdb_score.mean().round(2)],
["Thriller", thrillerDf.imdb_score.mean().round(2)],
["War", warDf.imdb_score.mean().round(2)],
["Western", westernDf.imdb_score.mean().round(2)]]

print genres