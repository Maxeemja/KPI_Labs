import math
import networkx as nx
import pandas as pd
import plotly.graph_objects as go


matrix_adjacency = [
    [0, 1, 1, 0, 0, 1],  # 1: connected to 2, 3, 6
    [1, 0, 0, 1, 1, 0],  # 2: connected to 1, 4, 5
    [1, 0, 0, 0, 1, 0],  # 3: connected to 1, 5
    [0, 1, 0, 0, 0, 1],  # 4: connected to 2, 6
    [0, 1, 1, 0, 0, 1],  # 5: connected to 2, 3, 6
    [1, 0, 0, 1, 1, 0]   # 6: connected to 1, 4, 5
]


positions = [
    (1, 2),    # 1
    (2, 2),    # 2
    (0, 1),    # 3
    (3, 1),    # 4
    (1, 0),    # 5
    (2, 0)     # 6
]


def add_cluster(graph, N_proc, matrix_adjacency):
    n_cluster = len(matrix_adjacency)
    for i in range(1, n_cluster + 1):
        graph.add_node((N_proc - 1) * n_cluster + i)
    for i in range(1, n_cluster + 1):
        for j in range(i + 1, n_cluster + 1):
            if matrix_adjacency[i - 1][j - 1] == 1:
                graph.add_edge((N_proc - 1) * n_cluster + i, (N_proc - 1) * n_cluster + j)
    return graph


def add_edges_regular(graph, N_proc, matrix_adjacency):
    if N_proc == 1:
        return graph

    n_cluster = len(matrix_adjacency)
    # Regular connections (4-2, 3-1)
    for current_proc in range(N_proc):
        left_child = 2 * current_proc + 1
        right_child = 2 * current_proc + 2

        if left_child < N_proc:
            # Connect to left child (blue connections)
            graph.add_edge(current_proc * n_cluster + 4, left_child * n_cluster + 2, color='blue')
            graph.add_edge(current_proc * n_cluster + 3, left_child * n_cluster + 1, color='blue')

        if right_child < N_proc:
            # Connect to right child (blue connections)
            graph.add_edge(current_proc * n_cluster + 4, right_child * n_cluster + 2, color='blue')
            graph.add_edge(current_proc * n_cluster + 3, right_child * n_cluster + 1, color='blue')

    return graph


def add_edges_irregular(graph, N_proc, matrix_adjacency):
    if N_proc == 1:
        return graph

    n_cluster = len(matrix_adjacency)

    # Calculate levels of the tree
    level = 0
    level_start = 0
    levels = []
    while level_start < N_proc:
        level_size = 2 ** level
        level_end = min(level_start + level_size, N_proc)
        levels.append(list(range(level_start + 1, level_end + 1)))
        level_start = level_end
        level += 1

    # Add green cross connections (6-4) and red connections (4-3) on even levels starting from level 1
    for current_level in range(1, len(levels), 2):
        current_level_nodes = levels[current_level]
        for i in range(0, len(current_level_nodes) - 1, 2):
            if i + 1 < len(current_level_nodes):
                node1 = current_level_nodes[i]
                node2 = current_level_nodes[i + 1]
                # Cross connections 6-4
                graph.add_edge((node1 - 1) * n_cluster + 6, (node2 - 1) * n_cluster + 4, color='green')
                graph.add_edge((node2 - 1) * n_cluster + 6, (node1 - 1) * n_cluster + 4, color='green')
                # Horizontal connection 4-3
                graph.add_edge((node1 - 1) * n_cluster + 4, (node2 - 1) * n_cluster + 3, color='red')

    return graph


def calculate_positions(N_proc, positions, x_scale=6, y_scale=6):
    tree_positions = {}
    level = 0
    level_start = 0
    while level_start < N_proc:
        level_size = 2 ** level
        level_end = min(level_start + level_size, N_proc)
        x_spacing = x_scale * 2 ** (math.ceil(math.log2(N_proc)) - level - 1)
        for i in range(level_start, level_end):
            x = (i - level_start) * x_spacing - (level_size - 1) * x_spacing / 2
            y = -level * y_scale
            tree_positions[i + 1] = (x, y)
        level_start = level_end
        level += 1

    cluster_positions = {}
    for node_id, (x, y) in tree_positions.items():
        for i, (dx, dy) in enumerate(positions):
            sub_node_id = (node_id - 1) * len(positions) + i + 1
            cluster_positions[sub_node_id] = (x + dx, y + dy)

    return cluster_positions


def draw_graph(graph, positions, node_size=5):
    edges_by_color = {
        'black': [],
        'blue': [],
        'red': [],
        'green': []
    }

    for u, v in graph.edges:
        color = graph[u][v].get('color', 'black')
        x0, y0 = positions[u]
        x1, y1 = positions[v]
        if color in edges_by_color:
            edges_by_color[color].append((x0, y0, x1, y1))

    fig = go.Figure()

    for color, edges in edges_by_color.items():
        for x0, y0, x1, y1 in edges:
            fig.add_trace(go.Scatter(
                x=[x0, x1], y=[y0, y1],
                mode='lines',
                line=dict(color=color, width=2),
                showlegend=False
            ))

    node_x, node_y = zip(*positions.values())
    node_text = [str(i) for i in range(1, len(node_x) + 1)]

    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        marker=dict(size=node_size, color='black'),
        text=node_text,
        textposition='top center',
        showlegend=False
    ))

    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )

    fig.show()


def calculate_metrics(graph):
    diameter = nx.diameter(graph)
    average_diameter = round(nx.average_shortest_path_length(graph), 5)
    degree = int(max(dict(graph.degree()).values()))
    cost = nx.number_of_edges(graph)
    traffic = round((2 * average_diameter) / degree, 5)
    return diameter, average_diameter, degree, cost, traffic


def main():
    N_proc = 15  # Number of processors
    metrics_table = pd.DataFrame(columns=['Кластери', 'Процесори', 'Діаметр',
                                          'Середній діаметр', 'Ступінь', 'Вартість', 'Топологічний трафік'])

    for i in range(1, N_proc + 1):
        graph = nx.Graph()
        for j in range(1, i + 1):
            graph = add_cluster(graph, j, matrix_adjacency)
        graph = add_edges_regular(graph, i, matrix_adjacency)
        graph = add_edges_irregular(graph, i, matrix_adjacency)

        diameter, average_diameter, degree, cost, traffic = calculate_metrics(graph)
        metrics_table = pd.concat([metrics_table, pd.DataFrame([{
            'Кластери': i,
            'Процесори': i * len(matrix_adjacency),
            'Діаметр': diameter,
            'Середній діаметр': average_diameter,
            'Ступінь': degree,
            'Вартість': cost,
            'Топологічний трафік': traffic
        }])], ignore_index=True)

    node_positions = calculate_positions(N_proc, positions)
    draw_graph(graph, node_positions)
    print(metrics_table.to_string(index=False))
    metrics_table.to_excel('metrics_table.xlsx', index=False)


if __name__ == '__main__':
    main()