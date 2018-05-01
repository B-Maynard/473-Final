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

yearHist = ggplot(df, aes(x="title_year")) +\
geom_histogram(binwidth=.05)

print yearHist
yearHist.save('yearHist.png')