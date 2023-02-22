import os
import pandas as pd

def GetFileDataFrame():
  entries = os.listdir('cache/files/')
  
  df = pd.DataFrame()

  for entry in entries:
    if os.path.isdir('cache/files/' + entry) == False:
      continue

    subentries = os.listdir('cache/files/' + entry)
    max_time = 0
    last_entry = None
    for subentry in subentries:
      time_m = os.path.getmtime('cache/files/' + entry + '/' + subentry)
      if (time_m > max_time):
        last_entry = 'cache/files/' + entry + '/' + subentry
    
    if last_entry is not None:
      record = {
        "user": entry,
        "file": last_entry
      }
      df = pd.concat([df, pd.DataFrame.from_records([record])])

  return df
