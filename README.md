# IMBD-Movie-Analysis
[Link to workbook](https://public.tableau.com/views/IMBD-Movie-Analysis/TrendsinMoviesoverTimeandGenre)<br>
Tableau workbook that breaks down trends in movie genres in terms of ratings and output.<br>
The workbook's objective is to examine how genre output has evolved over time and identify patterns in ratings. It depends upon a dataset that was cleaned and transformed in Python with pandas. The data was then analyzed with matplotlib and seaborn, and was finally made into visualizations in the Tableau workbook.<br>
## Data
Relies on the IMDb Movie Dataset: All Movies by Genre, licensed under CC BY-NC-SA 4.0, available at https://www.kaggle.com/datasets/rajugc/imdb-movies-dataset-based-on-genre.<br> The original dataset is a series of .csv files, seperated by genre, containing 360,000+ rows of individual movie data in total, from between 1911-2023. The movie_id, movie_name, year, rating, votes, and genre columns were chosen for analysis.
## Data Preparation, Feature Engineering, and Exploratory Analysis
Using pandas, the files were united into one data chart, narrowed to only include the six columns chosen for analysis, and then filtered to only include movie records with more than 1000 votes. Also, using cameras, a new data chart was made to record genre-level trends. Preliminary analysis of the data was carried out with matplotlib and seaborn.
## Dashboard
Finally, the data charts were used as data sources in Tableau to create a series of sheets, as well as a story documenting interesting trends in movie genres over the last century.
