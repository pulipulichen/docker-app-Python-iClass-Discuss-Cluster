import networkx as nx

def BuildNetwork(df):
  G = nx.Graph()

  df['value_norm'] = (df['value']-df['value'].min())/(df['value'].max()-df['value'].min())
  df['weight'] = 1 - df['value_norm']

  graph_df = df[['source', 'target', 'weight']]
  elist = list(graph_df.itertuples(index=False))
  G.add_weighted_edges_from(elist)

  # pos = nx.spring_layout(G)
  # # print(pos)
  # # nx.set_node_attributes(G, pos, name="pos")
  # for n, p in enumerate(pos):
  #   G.nodes[n]['pos'] = p

  return G