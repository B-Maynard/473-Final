import csv
from ggplot import *
import pandas as pd

#create a dataframe of movies and fill data from csv file
df = pd.read_csv('movie_metadata.csv')

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
print str(len(df)) + " rows"
print str(len(df.columns)) + " columns"

#Remove special character from movie title


#Plots
titleYearData = df['title_year']
minYear = min(titleYearData)
maxYear = max(titleYearData)

	
# g = ggplot(df, aes(title_year)) + geom_bar()

# print g