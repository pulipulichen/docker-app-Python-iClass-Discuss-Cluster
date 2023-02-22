import os
from datetime import datetime

def getModifiedTime(file):
  time = os.path.getmtime(file)
  time = datetime.fromtimestamp(time).strftime('%m/%d %H:%M:%S')
  return time

# 加上修改時間
def AppendTime(files):
  files['modified_time'] = files['file'].apply(getModifiedTime)
  
  return files
