import csv
from ggplot import *
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
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

#fill missing countries with a space
df['country'] = df['country'].fillna('')


#remove movies before 1980
df = df.drop(df[df.title_year < 1980].index)
df = df[np.isfinite(df['title_year'])]
print "After dropping movies before 1980 " +\
 str(len(df.title_year.index)) + " records remain"


##########################Visualisation#####################
#Plots

# #year released vs imdb score
yearScore = ggplot(df, aes(x="title_year", y='imdb_score')) + \
	geom_bar(aes(weight='title_year')) + \
	scale_x_date(breaks=date_breaks('36 months'))
print yearScore
#
#gross vs imdb score
grossScore = ggplot(df, aes(x="gross", y='imdb_score')) + \
	geom_point(color='steelblue')
print grossScore

#duration vs score
lengthScore = ggplot(df, aes(x="duration", y='imdb_score')) + \
	geom_point(color='steelblue')
print lengthScore

#content rating vs score
df.groupby('content_rating').imdb_score.mean().plot(kind='bar')
plt.show()
