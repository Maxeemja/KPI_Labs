import numpy as np
import pandas as pd


def build_cluster():
    edges = {
        1: [2, 3, 4],
        2: [1, 3, 6],
        3: [1, 2, 4],
        4: [1, 3, 9],
        5: [6, 7, 8],
        6: [2, 5, 7],
        7: [5, 6, 8],
        8: [5, 7, 11],
        9: [4, 10, 11, 12],
        10: [9, 11],
        11: [8, 9, 10, 12],
        12: [9, 11]
    }

    adjacency_matrix = np.zeros((12, 12), dtype=int)
    for node, neighbors in edges.items():
        for neighbor in neighbors:
            adjacency_matrix[node - 1, neighbor - 1] = 1
            adjacency_matrix[neighbor - 1, node - 1] = 1
    return adjacency_matrix


def connect_clusters(cluster_count):
    single_cluster = build_cluster()
    cluster_size = single_cluster.shape[0]
    total_nodes = cluster_count * cluster_size
    adjacency_matrix = np.zeros((total_nodes, total_nodes), dtype=int)

    # Place individual clusters
    for i in range(cluster_count):
        start = i * cluster_size
        end = start + cluster_size
        adjacency_matrix[start:end, start:end] = single_cluster

    # Connect clusters within each row (3 clusters per row)
    clusters_per_row = 3
    num_rows = (cluster_count + clusters_per_row - 1) // clusters_per_row

    for row in range(num_rows):
        row_start = row * clusters_per_row
        row_end = min(row_start + clusters_per_row, cluster_count)

        # Regular connections between adjacent clusters in the row
        for i in range(row_start, row_end - 1):
            current_start = i * cluster_size
            next_start = (i + 1) * cluster_size

            # Connect node 7 to node 9
            adjacency_matrix[current_start + 6, next_start + 8] = 1
            adjacency_matrix[next_start + 8, current_start + 6] = 1

            # Connect node 11 to node 1
            adjacency_matrix[current_start + 10, next_start] = 1
            adjacency_matrix[next_start, current_start + 10] = 1

        # Irregular connections between odd clusters (1st and 3rd) in the row
        if row_end - row_start >= 3:
            first_cluster = row_start * cluster_size
            third_cluster = (row_start + 2) * cluster_size

            # Connect node 3 to node 5
            adjacency_matrix[first_cluster + 2, third_cluster + 4] = 1
            adjacency_matrix[third_cluster + 4, first_cluster + 2] = 1

            # Connect node 10 to node 10
            adjacency_matrix[first_cluster + 9, third_cluster + 9] = 1
            adjacency_matrix[third_cluster + 9, first_cluster + 9] = 1

    # Add vertical connections between rows
    for row in range(num_rows - 1):
        current_row_start = row * clusters_per_row
        next_row_start = (row + 1) * clusters_per_row

        for i in range(clusters_per_row):
            if current_row_start + i >= cluster_count or next_row_start + i >= cluster_count:
                break

            current_cluster = (current_row_start + i) * cluster_size
            next_cluster = (next_row_start + i) * cluster_size

            # Connect node 12 to node 2 of cluster below
            adjacency_matrix[current_cluster + 11, next_cluster + 1] = 1
            adjacency_matrix[next_cluster + 1, current_cluster + 11] = 1

            # Connect node 12 to node 6 of cluster below
            adjacency_matrix[current_cluster + 11, next_cluster + 5] = 1
            adjacency_matrix[next_cluster + 5, current_cluster + 11] = 1

    return adjacency_matrix


def calculate_characteristics(adjacency_matrix):
    degrees = np.sum(adjacency_matrix, axis=1)
    max_degree = np.max(degrees)

    distances = floyd_warshall(adjacency_matrix)
    diameter = np.max(distances[distances != np.inf])
    average_diameter = np.mean(distances[distances != np.inf])

    topological_traffic = 2 * average_diameter / float(max_degree)
    cost = np.sum(adjacency_matrix) // 2

    return {
        "Кількість вершин": adjacency_matrix.shape[0],
        "Діаметр": diameter,
        "Середній діаметр": average_diameter,
        "Ступінь": max_degree,
        "Вартість": cost,
        "Трафік": topological_traffic
    }


def floyd_warshall(adjacency_matrix):
    n = adjacency_matrix.shape[0]
    distances = np.full((n, n), np.inf)
    np.fill_diagonal(distances, 0)

    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i, j]:
                distances[i, j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i, k] != np.inf and distances[k, j] != np.inf:
                    distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    return distances


def compute_local_gradient(data, param):
    return np.sum(data - param)


def distributed_gradient_descent(adjacency_matrix, data_splits, max_iter=3, learning_rate=0.01):
    num_nodes = adjacency_matrix.shape[0]
    params = np.zeros((num_nodes,))
    global_gradient = np.zeros((num_nodes,))

    for iteration in range(max_iter):
        print(f"\n--- Ітерація {iteration + 1} ---")

        local_gradients = []
        print("Паралельні локальні градієнтні обчислення:")
        for i, data in enumerate(data_splits):
            gradient = compute_local_gradient(data, params[i])
            local_gradients.append(gradient)
            print(f"Node {i + 1}: Local Gradient = {gradient:.4f}")

        print("\nПаралельна градієнтна агрегація:")
        for i in range(num_nodes):
            neighbors = np.where(adjacency_matrix[i] == 1)[0]
            global_gradient[i] = np.mean([local_gradients[j] for j in neighbors])
            print(f"Вузол {i + 1}: Агрегований градієнт = {global_gradient[i]:.4f}")

        print("\nПаралельне оновлення параметрів:")
        for i in range(num_nodes):
            params[i] -= learning_rate * global_gradient[i]
            print(f"Вузол {i + 1}: Оновлений параметр = {params[i]:.4f}")

    return params


if __name__ == "__main__":
    order = int(input("Введіть порядок топологічної організації: "))

    # Create a list to store characteristics for each scale
    all_characteristics = []

    # Calculate characteristics for each scale from 1 to order
    for scale in range(1, order + 1):
        clusters = 3 * scale  # 3 clusters per row, scaled by order
        adjacency_matrix = connect_clusters(clusters)
        characteristics = calculate_characteristics(adjacency_matrix)
        all_characteristics.append(characteristics)

        print(f"\nХарактеристики для масштабу {scale}:")
        for key, value in characteristics.items():
            print(f"{key}: {value}")

    # Create DataFrame and save to Excel
    df = pd.DataFrame(all_characteristics)

    # Round floating point numbers to 8 decimal places
    for col in df.columns:
        if df[col].dtype in ['float64', 'float32']:
            df[col] = df[col].round(8)

    # Save to Excel
    excel_filename = 'topology_characteristics.xlsx'
    df.to_excel(excel_filename, index=False)
    print(f"\nРезультати збережено у файл: {excel_filename}")

    # Continue with gradient descent if needed
    total_nodes = adjacency_matrix.shape[0]
    np.random.seed(42)
    data_splits = [np.random.rand(10) for _ in range(total_nodes)]

    final_params = distributed_gradient_descent(adjacency_matrix, data_splits)

    print("\nФінальні Параметри:")
    for i, param in enumerate(final_params):
        print(f"Вузол {i + 1}: {param:.4f}")