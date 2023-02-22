import networkx as nx
from networkx.algorithms import community

import pandas as pd

def getClusterDict(df_G):
  o = {}
  for (i,s) in enumerate(df_G):
    print(i)
    for sub in s:
      o[sub] = i
  return o

def ClusteringFiles(G):

  
  output = community.louvain_communities(G, weight='weight', resolution = 1.1, seed=123)
  
  cluster_dict = getClusterDict(output)
  return cluster_dict