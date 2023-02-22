import networkx as nx

def AddNodeAttributes(G, outliers, cluster_dict):
  nodes = G.nodes
  # print(nodes)

  outliers_dict = {}
  for node in nodes:
    outliers_dict[node] = (outliers.count(node) > 0)

  # print(outliers_dict)
  nx.set_node_attributes(G, outliers_dict, name="is_outlier")
  nx.set_node_attributes(G, cluster_dict, name="cluster")

  return G