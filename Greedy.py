import numpy as np
# from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import time

def draw_graph(hubungan,color): #untuk menampilkan graph
    t = time.process_time()
    G=nx.Graph()
    G.add_edges_from(hubungan)
    co = [color[i] for i in G.nodes()]
    nx.draw(G, node_size=1000/(len(hubungan)/10),node_color=co,
            with_labels=True,font_color='white')
    print(time.process_time()-t)
    plt.show()

def color_nodes(graph):
  # Order nodes in descending degree
  nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
  color_map = {}

  for node in nodes:
    available_colors = [True] * len(nodes)
    for neighbor in graph[node]:
      if neighbor in color_map:
        color = color_map[neighbor]
        available_colors[color] = False
    for color, available in enumerate(available_colors):
      if available:
        color_map[node] = color
        break

  return color_map


if __name__ == '__main__':
  graph = {
    'a': list('bcd'),
    'b': list('ac'),
    'c': list('abdef'),
    'd': list('ace'),
    'e': list('cdf'),
    'f': list('ce')
  }
  print(color_nodes(graph))

  # {'c': 0, 'a': 1, 'd': 2, 'e': 1, 'b': 2, 'f': 2}