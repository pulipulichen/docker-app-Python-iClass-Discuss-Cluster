def GetOutliers(df):
  df = df[df['is_outlier'] == True]

  
  sources = df['source'].tolist()
  targets = df['target'].tolist()

  outliers = sources + targets
  outliers = list(set(outliers))

  return outliers