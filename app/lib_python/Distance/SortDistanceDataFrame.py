
def SortDistanceDataFrame(files):
  files = files.sort_values(by=['is_outlier', 'cluster', 'modified_time'], ascending=False)
  return files