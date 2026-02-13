import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfMovies = pd.read_csv("data/df_movies.csv")
genreTrends = pd.read_csv("data/genre_trends.csv")
df = dfMovies.copy()
df["genre"] = df["genre"].str.split("|")
df = df.explode("genre")
topGenres = (
  df["genre"]
  .value_counts()
  .head(10)
  .index
)
filteredMovies = df[df["genre"].isin(topGenres)]
filteredTrends = genreTrends[genreTrends["genre"].isin(topGenres)]
plt.figure(figsize=(12, 6))
sns.lineplot(
  data=filteredTrends,
  x="year",
  y="avgRating",
  hue="genre"
)
plt.title("Average Movie Rating by Genre Over Time")
plt.show()
plt.figure(figsize=(12, 6))
sns.lineplot(
  data=filteredTrends,
  x="year",
  y="movieCount",
  hue="genre"
)
plt.title("Movie Count by Genre Over Time")
plt.show()
plt.figure(figsize=(12, 6))
sns.boxplot(
  data=filteredMovies,
  x="genre",
  y="rating"
)
plt.title("Rating Distribution by Genre")
plt.show()
plt.figure(figsize=(12, 6)) 
sns.scatterplot(
  data=filteredMovies,
  x="rating",
  y="votes"
)
plt.yscale("log")
plt.title("Rating and Vote Count")
plt.show()