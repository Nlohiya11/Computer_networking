import networkx as nx
import matplotlib.pyplot as plt


port = {
    'A': 6000,
    'B': 6001,
    'C': 6002,
    'D': 6003,
    'E': 6004,
    'F': 6005,
}
import random

G = nx.gnm_random_graph(6, 8)
for (u, v, w) in G.edges(data=True):
    w['weight'] = random.randint(1, 5)

mapping = {0: "A", 1: "B", 2: "C", 3: 'D', 4: "E", 5: 'F', 6: 'G'}
G = nx.relabel_nodes(G, mapping)

plt.figure(figsize=(7, 7))
pos = nx.spring_layout(G)

nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.3)
plt.show()

port = {
    'A': 6000,
    'B': 6001,
    'C': 6002,
    'D': 6003,
    'E': 6004,
    'F': 6005,
}

for node in G.nodes():
    f = open("{}config.txt".format(node), "w")
    neighbours = G[node]
    f.write(str(len(neighbours)))
    f.write("\n")
    for i in neighbours:
        f.write("{} {} {}\n".format(i, G[node][i]['weight'], port[i]))
for i in port.keys():
    print(nx.single_source_dijkstra(G, source=i))
