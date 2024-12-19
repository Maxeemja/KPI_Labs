import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

base_pos = {
    1: (1, 2), 2: (0, 1), 3: (2, 1), 4: (0, 0),
    5: (1, 0), 6: (2, 0)
}

num_graphs = 4
radius = num_graphs

graphs = [nx.Graph() for _ in range(num_graphs)]

edges = [
    (1, 2), (1, 3), (2, 3), (2, 4), (2, 5),
    (4, 5), (3, 5), (3, 6), (5, 6)
]

for g in graphs:
    g.add_nodes_from(range(1, 7))
    g.add_edges_from(edges)

center_x = np.mean([coord[0] for coord in base_pos.values()])
center_y = np.mean([coord[1] for coord in base_pos.values()])
central_graph_pos = {node: (base_pos[node][0] - center_x, base_pos[node][1] - center_y) for node in base_pos}
combined_pos = {}
combined_pos.update({(0, node): coord for node, coord in central_graph_pos.items()})

for i in range(1, num_graphs):
    angle = -360 / (num_graphs - 1) * (i - 1) + 90
    shift_x = radius * np.cos(np.radians(angle))
    shift_y = radius * np.sin(np.radians(angle))

    graph_pos = {}
    for node, (x, y) in base_pos.items():
        graph_pos[node] = (x + shift_x, y + shift_y)

    rotation_angle_deg = -360 / (num_graphs - 1) * (i - 1)
    rotated_graph_pos = {}
    for node, (x, y) in graph_pos.items():
        centered_x = x - shift_x
        centered_y = y - shift_y
        rotated_x = centered_x * np.cos(np.radians(rotation_angle_deg)) - centered_y * np.sin(
            np.radians(rotation_angle_deg))
        rotated_y = centered_x * np.sin(np.radians(rotation_angle_deg)) + centered_y * np.cos(
            np.radians(rotation_angle_deg))
        rotated_graph_pos[node] = (rotated_x + shift_x, rotated_y + shift_y)

    combined_pos.update({(i, node): coord for node, coord in rotated_graph_pos.items()})

combined_graph = nx.Graph()
for i, g in enumerate(graphs):
    relabeled_nodes = {node: (i, node) for node in g.nodes}
    nx.relabel_nodes(g, relabeled_nodes, copy=False)
    combined_graph = nx.compose(combined_graph, g)

# Modified regular connections
regular_edges = []
for i in range(1, num_graphs):
    combined_graph.add_edge((0, 4), (i, 4))
    combined_graph.add_edge((0, 6), (i, 6))
    regular_edges.append(((0, 4), (i, 4)))
    regular_edges.append(((0, 6), (i, 6)))

# Modified irregular connections between neighbors
irregular_edges = []
if num_graphs > 2:
    for i in range(1, num_graphs - 1):
        combined_graph.add_edge((i, 2), (i + 1, 1))
        irregular_edges.append(((i, 2), (i + 1, 1)))
    combined_graph.add_edge((num_graphs - 1, 2), (1, 1))
    irregular_edges.append(((num_graphs - 1, 2), (1, 1)))

plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(combined_graph, combined_pos, node_color="lightblue", node_size=300)

internal_edges = [(u, v) for u, v in combined_graph.edges if u[0] == v[0]]
nx.draw_networkx_edges(
    combined_graph, combined_pos, edgelist=internal_edges, edge_color="black", width=1,
)

nx.draw_networkx_edges(
    combined_graph, combined_pos, edgelist=regular_edges, edge_color="red", width=2,
)

nx.draw_networkx_edges(
    combined_graph, combined_pos, edgelist=irregular_edges, edge_color="blue",
    width=2, arrows=True, arrowstyle="-",
    connectionstyle="arc3,rad=0.2",
)

nx.draw_networkx_labels(
    combined_graph, combined_pos, {node: str(node[1]) for node in combined_graph.nodes}, font_size=10
)

diameter = nx.diameter(combined_graph)
average_diameter = round(nx.average_shortest_path_length(combined_graph), 2)
degree = max(dict(combined_graph.degree()).values())
cost = combined_graph.number_of_edges()
topological_traffic = round((2 * average_diameter) / degree, 2)

print("Топологічні характеристики графа:")
print(f"Кластери: {num_graphs}")
print(f"Вершини: {combined_graph.number_of_nodes()}")
print(f"Діаметр: {diameter}")
print(f"Середній діаметр: {average_diameter}")
print(f"Максимальний ступінь: {degree}")
print(f"Вартість (кількість ребер): {cost}")
print(f"Топологічний трафік: {topological_traffic}")
plt.show()