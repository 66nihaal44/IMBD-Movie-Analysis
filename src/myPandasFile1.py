import pandas as pd
from glob import glob
import os

files = glob("data/*.csv")
dfs = []
for f in files:
  genre = os.path.splitext(os.path.basename(f))[0]
  df = pd.read_csv(f)
  df["genre"] = genre
  dfs.append(df)
dfAll = pd.concat(dfs, ignore_index=True)
print("dfAll shape: ", dfAll.shape)
print("sum: ", dfAll.duplicated().sum())
dfAll = dfAll.drop_duplicates()
dfAll = dfAll[dfAll["votes"] >= 1000]
dfMovies = (
  dfAll
  .groupby("movie_id", as_index=False)
  .agg({
    "movie_name":"first",
    "year":"first",
    "rating":"first",
    "votes":"first",
    "genre":lambda x: "|".join(sorted(pd.unique(x)))
  })
)
print(dfMovies["movie_id"].is_unique)
print("The mean:", dfMovies["genre"].str.contains("\\|").mean())
print(dfAll.shape, dfMovies.shape)
dfMovies["genre"] = dfMovies["genre"].str.split("|")
dfMovies = dfMovies.explode("genre")
dfMovies.to_csv("data/df_movies.csv", index = False)
