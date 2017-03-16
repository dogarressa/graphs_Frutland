import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
n=input()

def read_data(filename):
    f=open(filename, 'r')
    return f.readlines()

lines=read_data("cities.txt")
for l in lines:
    a, b, weight = l.split()
    G.add_edge(a, b, weight=int(weight))

for i in nx.nodes(G):
    if not nx.has_path(G, n, i):
        print('there is no path')
    else:
        length,path=nx.bidirectional_dijkstra(G, n, i)
        print(length,path)
