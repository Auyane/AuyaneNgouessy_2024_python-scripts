"""
@author: Bertille AUYANE NGOUESSY EP OVONO 
Institution: Vaal University of Technology

"""


import pandas as pd

#excel_file = 'movie_dataset.csv'
df_csv = pd.read_csv('movie_dataset.csv')

print(df_csv)

new_csv = df_csv.to_csv(index=False)

# Group the movies by author and year, count the number of movies for each author in each year
grouped_df = df_csv.groupby(['Actors', 'Year']).size().reset_index(name='num_movies')

# Sort the grouped DataFrame by author, year, and the number of movies
sorted_df = grouped_df.sort_values(by=['Actors', 'Year', 'num_movies'], ascending=[True, True, False])

print(sorted_df)

####Question 1:Highest rated movie: is The Dark Knight with 9.0 rating
    
# Find the index of the row with the highest rating
highest_rated_index = df_csv['Rating'].idxmax()

# Get the details of the highest rated movie
highest_rated_movie = df_csv.loc[highest_rated_index]

print("Highest rated movie:")
print(highest_rated_movie)

### Question 2: Average revenue of all movies: 82.95637614678898 therefor
# it is between 70 Million and 100 Millions
    
# Calculate the average revenue of all movies
average_revenue_all_movies = df_csv['Revenue (Millions)'].mean()

print("Average revenue of all movies:", average_revenue_all_movies)


### Question 3: Average revenue of movies from 2015 to 2017: 63.099905660377345
## so it is less than 40 Millions

# Filter the DataFrame for movies released between 2015 and 2017
movies_2015_to_2017 = df_csv[(df_csv['Year'] >= 2015) & (df_csv['Year'] <= 2017)]

# Calculate the average revenue of movies released between 2015 and 2017
average_revenue_2015_to_2017 = movies_2015_to_2017['Revenue (Millions)'].mean()

print("Average revenue of movies from 2015 to 2017:", average_revenue_2015_to_2017)


### Question 4:Number of movies released in 2016: 297

# Filter the DataFrame for movies released in the year 2016
movies_2016 = df_csv[df_csv['Year'] == 2016]

# Count the number of movies released in 2016
num_movies_2016 = movies_2016.shape[0]

print("Number of movies released in 2016:", num_movies_2016)

### Question 5: Number of movies directed by Christopher Nolan: 5

# Filter the DataFrame for movies directed by Christopher Nolan
nolan_movies = df_csv[df_csv['Director'] == 'Christopher Nolan']

# Count the number of movies directed by Christopher Nolan
num_nolan_movies = nolan_movies.shape[0]

print("Number of movies directed by Christopher Nolan:", num_nolan_movies)


### Question 6: Number of movies with a rating of at least 8: 78

# Filter the DataFrame for movies with a rating of at least 8
high_rated_movies = df_csv[df_csv['Rating'] >= 8]

# Count the number of movies with a rating of at least 8
num_high_rated_movies = high_rated_movies.shape[0]

print("Number of movies with a rating of at least 8:", num_high_rated_movies)   


#### Question 7: Filter the data for movies directed by Christopher Nolan: 8.6

nolan_movies = df_csv[df_csv['Director'] == 'Christopher Nolan']

# Calculate the median rating of Christopher Nolan's movies
median_rating_nolan_movies = nolan_movies['Rating'].median()

print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan_movies)


#### Question 8: Year with the highest average rating:2007


average_rating_per_year = df_csv.groupby('Year')['Rating'].mean()

# Identify the year with the highest average rating
year_highest_average_rating = average_rating_per_year.idxmax()
highest_average_rating = average_rating_per_year.max()

print("Year with the highest average rating:", year_highest_average_rating)
print("Highest average rating:", highest_average_rating)

#### Question 9: Percentage increase in the number of movies from 2006 to 2016
# is 575.0 %

# Filter the DataFrame for the years between 2006 and 2016
filtered_df = df_csv[(df_csv['Year'] >= 2006) & (df_csv['Year'] <= 2016)]

# Count the number of movies for each year
movies_per_year = filtered_df['Year'].value_counts().sort_index()

# Calculate the percentage increase from 2006 to 2016
movies_2006 = movies_per_year[2006]
movies_2016 = movies_per_year[2016]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print("Percentage increase in the number of movies from 2006 to 2016:", round(percentage_increase, 2), "%")

#### Question 10:Most common actor:Mark Wahlberg
    
df = pd.read_csv("movie_dataset.csv")

# Count the occurrences of each actor
actor_counts = df['Actors'].value_counts()

# Get the most common actor
most_common_actor = actor_counts.idxmax()
num_movies_most_common_actor = actor_counts.max()

print("Most common actor:", most_common_actor)
print("Number of movies:", num_movies_most_common_actor)
# Count the occurrences of each actor
actor_counts = df_csv['Actors'].value_counts()

# Get the most common actor
most_common_actor = actor_counts.idxmax()
num_movies_most_common_actor = actor_counts.max()

print("Most common actor:", most_common_actor)
print("Number of movies:", num_movies_most_common_actor)


#### Question 11:Number of unique genres: 207

unique_genres = df_csv['Genre'].unique()

# Get the number of unique genres
num_unique_genres = len(unique_genres)

print("Number of unique genres:", num_unique_genres)

### Question 12: 
    
# Select only numerical columns for correlation analysis
numerical_df = df.select_dtypes(include=['int64', 'float64'])

# Calculate the correlation matrix
correlation_matrix = numerical_df.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Insights and Recommendations:
# 1. Positive correlation between budget and revenue indicates that higher budget movies tend to generate higher revenue.
# 2. Positive correlation between budget and runtime suggests that longer movies may require higher budgets.
# 3. Weak correlation between rating and revenue implies that high ratings do not guarantee higher revenue.
# 4. Weak correlation between rating and budget indicates that a movie's budget may not significantly impact its rating.
# 5. Positive correlation between popularity and revenue suggests that popular movies tend to perform better financially.

# Advice for Directors to Produce Better Movies:
# - Focus on creating engaging and captivating storylines that resonate with the audience.
# - Invest in quality production values without solely relying on high budgets.
# - Pay attention to audience feedback and preferences to gauge potential success.
# - Collaborate with talented actors, writers, and crew members to elevate the overall quality of the movie.
# - Prioritize innovation and creativity to distinguish the movie from competitors and offer a unique viewing experience.

### Question 13:
    
# Assume the Python file "css4p01.py" contains the code for data analysis and clearing

# Analyze and clear the data (example code)
import pandas as pd

# Load the dataset
df = pd.read_csv("movie_dataset.csv")

# Perform data analysis and cleaning
# For example:
# - Data exploration
# - Data cleaning (handling missing values, removing duplicates, etc.)
# - Data transformation (feature engineering, encoding categorical variables, etc.)

# Save the cleaned data to a new CSV file
df.to_csv("cleaned_movie_dataset.csv", index=False)

# Output the URL link to the Python file
username = "your_username"
repository_name = "python-scripts"
file_name = "css4p01.py"
url = f"https://github.com/{username}/{repository_name}/blob/main/{file_name}"
print("URL link to the Python file:", url)
