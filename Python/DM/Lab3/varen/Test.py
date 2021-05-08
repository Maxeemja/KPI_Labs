import networkx as nx
import matplotlib.pyplot as plt
from copy import copy
V = 5
nodes = [0, 1, 2, 3, 4]
graph = {(1,2):3, (2,1):3, (0,4):5, (4,0):5, (3,4):6, (4,3):6, (2,3):4, (3,2):4, (0,1):20, (1,0):20}
graph1 = [(1,2,3), (2,1,3), (0,4,5), (4,0,5), (3,4,6), (4,3,6), (2,3,4), (3,2,4), (0,1,6), (1,0,6)]
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(graph.keys())
nx.draw_shell(G, with_labels=True)
nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels=graph, label_pos=0.1)
plt.show()
def bellmanFord(src, dest):
    dist = [float("Inf")] * V
    prev = [None]*V
    dist[src] = 0
    for i in range(V - 1):
        for key in graph.keys():
            if dist[key[0]] + graph[key] < dist[key[1]]:
                dist[key[1]] = dist[key[0]] + graph[key]
                prev[key[1]] = key[0]
            if dist[key[1]] + graph[key] < dist[key[0]]:
                dist[key[0]] = dist[key[1]] + graph[key]
                prev[key[0]] = key[1]
    print(dist)
    for i in range(V):
        print("{} -> {}".format(i, dist[i]))
    print(prev)
    curr = dest
    path = []
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    print(path)
    pathedges = []
    for i in range(len(path)-1):
        pathedges.append((path[i], path[i+1]))
    print(pathedges)
    G.add_nodes_from(nodes)
    G.add_edges_from(graph.keys())
    nx.draw_shell(G, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels=graph, label_pos=0.1)
    nx.draw_networkx_edges(G, pos=nx.shell_layout(G) ,edgelist=pathedges, edge_color="yellow")
    plt.show()
bellmanFord(0, 1)
