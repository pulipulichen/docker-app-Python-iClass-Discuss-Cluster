
import os

def getFilesize(file):
  file_stats = os.stat(file)
  return file_stats.st_size / (1024 * 1024)

def AppendSize(files):
  files['filesize'] = files['file'].apply(getFilesize)
  return files
