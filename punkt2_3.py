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

St=nx.minimum_spanning_tree(G)
nx.draw(St)
plt.show()
