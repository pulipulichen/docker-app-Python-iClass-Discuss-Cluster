import numpy as np

def CalcDistanceOutlier(df):
  # print(len(find_outliers_IQR(df['value'])))

  values = df['value']
  q1 = values.quantile(0.25)
  q3 = values.quantile(0.75)
  IQR = q3 - q1
  down_bound = int(q1 - 1.5 * IQR)
  # up_bound = q3 + 1.5 * IQR

  # df['is_outlier'] = df[df['value'] < down_bound]
  df['is_outlier'] = np.where(df['value'] < down_bound, True, False)

  return df