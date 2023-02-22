import networkx as nx
import json

def SaveCYJS(G, filename):
  cyjs = nx.cytoscape_data(G)

  # pos = nx.spring_layout(G)
  # nodes = cyjs['elements']['nodes']
  # for node in nodes:
  #   data = node['data']
  #   id = data['id']

  #   node["position"] = {}
  #   node["position"]["x"] = pos[id][0]
  #   node["position"]["y"] = pos[id][1]
  # cyjs['elements']['nodes'] = nodes

  cyjs = json.dumps(cyjs, ensure_ascii=False)

  text_file = open('input/' + filename + ".cyjs", "w", encoding='utf-8')
  n = text_file.write(cyjs)
  text_file.close()