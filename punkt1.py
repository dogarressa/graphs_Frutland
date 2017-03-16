import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

def read_data(filename):
    f=open(filename, 'r')
    return f.readlines()

lines=read_data("cities.txt")
for l in lines:
    a, b, weight = l.split()
    G.add_edge(a, b, weight=int(weight))

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=50)
nx.draw_networkx_edges(G, pos, width=1)
plt.axis('off')
plt.savefig("weighted_graph.png")
plt.show()
