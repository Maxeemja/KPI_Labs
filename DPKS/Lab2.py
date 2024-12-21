import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def create_topology(num_clusters):
    base_pos = {
        1: (1, 2), 2: (0, 1), 3: (2, 1), 4: (0, 0),
        5: (1, 0), 6: (2, 0)
    }

    radius = max(5, num_clusters)
    graphs = [nx.Graph() for _ in range(num_clusters)]

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

    for i in range(1, num_clusters):
        angle = -360 / (num_clusters - 1) * (i - 1) + 90 if num_clusters > 1 else 0
        shift_x = radius * np.cos(np.radians(angle))
        shift_y = radius * np.sin(np.radians(angle))

        graph_pos = {}
        for node, (x, y) in base_pos.items():
            graph_pos[node] = (x + shift_x, y + shift_y)

        rotation_angle_deg = -360 / (num_clusters - 1) * (i - 1) if num_clusters > 1 else 0
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

    regular_edges = []
    irregular_edges = []

    # Modified regular connections
    for i in range(1, num_clusters):
        combined_graph.add_edge((0, 4), (i, 4))
        combined_graph.add_edge((0, 6), (i, 6))
        regular_edges.append(((0, 4), (i, 4)))
        regular_edges.append(((0, 6), (i, 6)))

    # Modified irregular connections between neighbors
    if num_clusters > 2:
        for i in range(1, num_clusters - 1):
            combined_graph.add_edge((i, 2), (i + 1, 1))
            irregular_edges.append(((i, 2), (i + 1, 1)))
        combined_graph.add_edge((num_clusters - 1, 2), (1, 1))
        irregular_edges.append(((num_clusters - 1, 2), (1, 1)))

    return combined_graph, combined_pos, regular_edges, irregular_edges


def calculate_metrics(graph):
    diameter = nx.diameter(graph)
    average_diameter = round(nx.average_shortest_path_length(graph), 4)
    degree = max(dict(graph.degree()).values())
    cost = graph.number_of_edges()
    topological_traffic = round((2 * average_diameter) / degree, 4)
    return {
        'nodes': graph.number_of_nodes(),
        'diameter': diameter,
        'degree': degree,
        'avg_diameter': average_diameter,
        'cost': cost,
        'traffic': topological_traffic
    }


# Print table header
print("\n{:^10} {:^10} {:^12} {:^12} {:^12} {:^10} {:^10}".format(
    "Clusters", "Nodes", "Diameter", "Degree", "Av.Diameter", "Cost", "Traffic"
))
print("-" * 76)

# Calculate and print metrics for each step
max_clusters = 20
for step in range(1, max_clusters + 1):
    graph, pos, reg_edges, irreg_edges = create_topology(step)
    metrics = calculate_metrics(graph)

    print("{:^10} {:^10} {:^12} {:^12} {:^12.4f} {:^10} {:^10.4f}".format(
        step,
        metrics['nodes'],
        metrics['diameter'],
        metrics['degree'],
        metrics['avg_diameter'],
        metrics['cost'],
        metrics['traffic']
    ))

# Visualize the final topology
final_graph, final_pos, final_regular_edges, final_irregular_edges = create_topology(max_clusters)

plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(final_graph, final_pos, node_color="lightblue", node_size=300)

internal_edges = [(u, v) for u, v in final_graph.edges if u[0] == v[0]]
nx.draw_networkx_edges(
    final_graph, final_pos, edgelist=internal_edges, edge_color="black", width=1,
)

nx.draw_networkx_edges(
    final_graph, final_pos, edgelist=final_regular_edges, edge_color="red", width=2,
)

nx.draw_networkx_edges(
    final_graph, final_pos, edgelist=final_irregular_edges, edge_color="blue",
    width=2, arrows=True, arrowstyle="-",
    connectionstyle="arc3,rad=0.2",
)

nx.draw_networkx_labels(
    final_graph, final_pos, {node: str(node[1]) for node in final_graph.nodes}, font_size=10
)

plt.show()