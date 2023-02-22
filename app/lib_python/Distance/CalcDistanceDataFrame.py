from itertools import combinations
from fastDamerauLevenshtein import damerauLevenshtein
import pandas as pd
# from .CalcDistanceOutlier import *
# from .ClusteringFiles import *
# from .SortDistanceDataFrame import *

def CalcDistanceDataFrame(files):
  df = pd.DataFrame()

  pairs = list(combinations(range(0, len(files)),2))
  for pair in pairs:
    # print(str(pair[0]) + '-' + str(pair[1]))
    
    source = files.iloc[[pair[0]]].to_dict('records')[0]
    target = files.iloc[[pair[1]]].to_dict('records')[0]
    distance = damerauLevenshtein(source['data'], target['data'], similarity=False)
    record = {
      "source": source["user"],
      "target": target["user"],
      "value": distance
    }
    df = pd.concat([df, pd.DataFrame.from_records([record])])
  
  # print(df)
  # return False
  
  # df = CalcDistanceOutlier(df)

  # # print(df)
  # # return False
  # {files, cyjs} = ClusteringFiles(df, files)

  # files = SortDistanceDataFrame(files)
  return df