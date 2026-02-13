import pandas as pd

dfMovies = pd.read_csv("data/df_movies.csv")

genreTrends = (
  dfMovies.groupby(["year", "genre"])
  .agg(
    avgRating=("rating","mean"),
    movieCount=("movie_name","count")
  )
  .reset_index()
)
genreTrends["rollingRating"] = (
  genreTrends
  .groupby("genre")["avgRating"]
  .transform(lambda x: x.rolling(5, min_periods=1).mean())
)
genreTrends.to_csv("data/genre_trends.csv", index=False)