import os
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def clean_basics(basics):
  basics = basics.dropna(subset=['primaryTitle', 'originalTitle'])

  basics.loc[2989193, ['primaryTitle', 'originalTitle', 'isAdult']] = ['Bay of the Triffids/Doctor of Doom', 'Bay of the Triffids/Doctor of Doom', 0]

  basics_isAdult_filter = basics[~basics['isAdult'].isin([0,1])]
  basics_isAdult_filter['startYear'] = basics_isAdult_filter['isAdult']
  basics_isAdult_filter['isAdult'] = basics_isAdult_filter['originalTitle']
  basics_isAdult_filter[['primaryTitle', 'originalTitle']] = basics_isAdult_filter['primaryTitle'].str.split('\t', expand=True)
  basics.loc[basics_isAdult_filter.index] = basics_isAdult_filter

  basics['isAdult'] = pd.to_numeric(basics['isAdult'])
  basics = basics[basics['isAdult'] == 0]

  basics['genres'] = basics['genres'].str.replace(r',', r', ')

  basics["isAdult"] = pd.to_numeric(basics["isAdult"], errors="coerce").astype("Int64")
  basics["startYear"] = pd.to_numeric(basics["startYear"], errors="coerce").astype("Int64")
  basics["endYear"] = pd.to_numeric(basics["endYear"], errors="coerce").astype("Int64")

  misplaced_genres = ['Reality-TV', 'Talk-Show', 'Documentary','Family,Game-Show','Animation,Comedy,Family','News,Talk-Show','Comedy,News,Talk-Show','Documentary,Reality-TV','Comedy,Drama,Fantasy','Fantasy,Horror,Mystery','Action,Fantasy,Horror', 'Action,Horror,Mystery','Comedy,Drama,Horror','Action,Adventure,Drama','Drama,Fantasy,Horror','Game-Show,Reality-TV']
  basics_misplaced_genres = basics[basics['runtimeMinutes'].isin(misplaced_genres)]

  basics_misplaced_genres['genres'] = basics_misplaced_genres['runtimeMinutes']
  basics_misplaced_genres['runtimeMinutes'] = float('nan')
  basics.loc[basics_misplaced_genres.index] = basics_misplaced_genres

  basics["runtimeMinutes"] = pd.to_numeric(basics["runtimeMinutes"], errors="coerce").astype("Int64")

  return basics

def clean_episode(episode):
  episode.dropna(inplace=True)

  episode['seasonNumber'] = episode['seasonNumber'].astype(int)
  episode['episodeNumber'] = episode['episodeNumber'].astype(int)

def merge_and_export(basics, ratings, episode):
  all_ratings = pd.merge(basics, ratings, on='tconst', how='inner')

  valid_tconsts = set(all_ratings['tconst'])
  all_episodes = episode[
    episode['tconst'].isin(valid_tconsts) & episode['parentTconst'].isin(valid_tconsts)
  ]

  all_ratings = all_ratings[
    all_ratings['tconst'].isin(all_episodes['tconst']) | all_ratings['tconst'].isin(all_episodes['parentTconst'])
  ]

  all_series = all_ratings[all_ratings['tconst'].isin(all_episodes['parentTconst'])]
  all_episodes = pd.merge(all_episodes, all_ratings, on='tconst', how='inner')

  os.makedirs("/preprocessed", exist_ok=True)
  all_episodes.to_csv('preprocessed/episodes.csv', index=False)
  all_series.to_csv('preprocessed/series.csv', index=False)

if __name__ == "__main__":
  basics = pd.read_csv('raw/title.basics.tsv', sep='\t', low_memory=False, na_values=['\\N'])
  episode = pd.read_csv('raw/title.episode.tsv', sep='\t', low_memory=False, na_values=['\\N'])
  ratings = pd.read_csv('raw/title.ratings.tsv', sep='\t', low_memory=False, na_values=['\\N'])

  basics = clean_basics(basics)
  episode = clean_episode(episode)
  merge_and_export(basics, ratings, episode)
