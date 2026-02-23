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
dfAll = dfAll.loc[:, ["movie_id", "movie_name", "year", "rating", "votes", "genre"]]
print("sum: ", dfAll.duplicated().sum())
dfAll = dfAll.drop_duplicates()
dfAll = dfAll[dfAll["votes"] >= 1000]
print(dfAll.shape)
dfAll.to_csv("data/df_movies.csv", index = False)