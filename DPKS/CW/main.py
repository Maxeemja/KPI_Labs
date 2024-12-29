import numpy as np
import pandas as pd


class Topology:
    def __init__(self, cluster_count):
        self.cluster_count = cluster_count
        self.cluster_size = 12
        self.adjacency_matrix = self.create_full_adjacency_matrix()

    def create_cluster(self):
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

        matrix = np.zeros((self.cluster_size, self.cluster_size), dtype=int)
        for node, neighbors in edges.items():
            for neighbor in neighbors:
                matrix[node - 1, neighbor - 1] = 1
                matrix[neighbor - 1, node - 1] = 1
        return matrix

    def create_full_adjacency_matrix(self):
        base_cluster = self.create_cluster()
        total_nodes = self.cluster_count * self.cluster_size
        full_matrix = np.zeros((total_nodes, total_nodes), dtype=int)

        for i in range(self.cluster_count):
            start = i * self.cluster_size
            end = start + self.cluster_size
            full_matrix[start:end, start:end] = base_cluster

        self.connect_clusters_in_rows(full_matrix)
        self.connect_clusters_between_rows(full_matrix)

        return full_matrix

    def connect_clusters_in_rows(self, matrix):
        clusters_per_row = 3
        for row in range((self.cluster_count + clusters_per_row - 1) // clusters_per_row):
            row_start = row * clusters_per_row
            row_end = min(row_start + clusters_per_row, self.cluster_count)

            for i in range(row_start, row_end - 1):
                current_start = i * self.cluster_size
                next_start = (i + 1) * self.cluster_size

                # Connect node 7 to node 9
                matrix[current_start + 6, next_start + 8] = 1
                matrix[next_start + 8, current_start + 6] = 1

                # Connect node 11 to node 1
                matrix[current_start + 10, next_start] = 1
                matrix[next_start, current_start + 10] = 1

            if row_end - row_start >= 3:
                first_cluster = row_start * self.cluster_size
                third_cluster = (row_start + 2) * self.cluster_size

                # Connect node 3 to node 5
                matrix[first_cluster + 2, third_cluster + 4] = 1
                matrix[third_cluster + 4, first_cluster + 2] = 1

                # Connect node 10 to node 10
                matrix[first_cluster + 9, third_cluster + 9] = 1
                matrix[third_cluster + 9, first_cluster + 9] = 1

    def connect_clusters_between_rows(self, matrix):
        for row in range((self.cluster_count + 2) // 3 - 1):
            current_row_start = row * 3
            next_row_start = (row + 1) * 3

            for i in range(3):
                if current_row_start + i >= self.cluster_count or next_row_start + i >= self.cluster_count:
                    break

                current_cluster = (current_row_start + i) * self.cluster_size
                next_cluster = (next_row_start + i) * self.cluster_size

                matrix[current_cluster + 11, next_cluster + 1] = 1
                matrix[next_cluster + 1, current_cluster + 11] = 1

                matrix[current_cluster + 11, next_cluster + 5] = 1
                matrix[next_cluster + 5, current_cluster + 11] = 1

    def calculate_characteristics(self):
        degrees = np.sum(self.adjacency_matrix, axis=1)
        max_degree = np.max(degrees)
        distances = self.floyd_warshall()
        diameter = np.max(distances[distances != np.inf])
        avg_diameter = np.mean(distances[distances != np.inf])
        topological_traffic = 2 * avg_diameter / float(max_degree)
        cost = np.sum(self.adjacency_matrix) // 2

        return {
            "Кількість вершин": self.adjacency_matrix.shape[0],
            "Діаметр": diameter,
            "Середній діаметр": avg_diameter,
            "Ступінь": max_degree,
            "Вартість": cost,
            "Трафік": topological_traffic
        }

    def floyd_warshall(self):
        n = self.adjacency_matrix.shape[0]
        dist = np.full((n, n), np.inf)
        np.fill_diagonal(dist, 0)

        for i in range(n):
            for j in range(n):
                if self.adjacency_matrix[i, j]:
                    dist[i, j] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i, k] != np.inf and dist[k, j] != np.inf:
                        dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])

        return dist


class GradientDescent:
    def __init__(self, adjacency_matrix, data_splits, max_iter=3, learning_rate=0.01):
        self.adjacency_matrix = adjacency_matrix
        self.data_splits = data_splits
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.num_nodes = adjacency_matrix.shape[0]
        self.params = np.zeros((self.num_nodes,))
        self.global_gradient = np.zeros((self.num_nodes,))

    def compute_local_gradient(self, data, param):
        return np.sum(data - param)

    def run(self):
        for iteration in range(self.max_iter):
            print(f"\n--- Ітерація {iteration + 1} ---")
            local_gradients = self.compute_local_gradients()
            self.aggregate_gradients(local_gradients)
            self.update_parameters()

        return self.params

    def compute_local_gradients(self):
        local_gradients = []
        print("Паралельні локальні градієнтні обчислення:")
        for i, data in enumerate(self.data_splits):
            gradient = self.compute_local_gradient(data, self.params[i])
            local_gradients.append(gradient)
            print(f"Node {i + 1}: Local Gradient = {gradient:.4f}")
        return local_gradients

    def aggregate_gradients(self, local_gradients):
        print("\nПаралельна градієнтна агрегація:")
        for i in range(self.num_nodes):
            neighbors = np.where(self.adjacency_matrix[i] == 1)[0]
            self.global_gradient[i] = np.mean([local_gradients[j] for j in neighbors])
            print(f"Вузол {i + 1}: Агрегований градієнт = {self.global_gradient[i]:.4f}")

    def update_parameters(self):
        print("\nПаралельне оновлення параметрів:")
        for i in range(self.num_nodes):
            self.params[i] -= self.learning_rate * self.global_gradient[i]
            print(f"Вузол {i + 1}: Оновлений параметр = {self.params[i]:.4f}")


def main():
    order = int(input("Введіть порядок топологічної організації: "))
    all_characteristics = []

    for scale in range(1, order + 1):
        topology = Topology(cluster_count=3 * scale)
        characteristics = topology.calculate_characteristics()
        all_characteristics.append(characteristics)

        print(f"\nХарактеристики для масштабу {scale}:")
        for key, value in characteristics.items():
            print(f"{key}: {value}")

    df = pd.DataFrame(all_characteristics)

    for col in df.columns:
        if df[col].dtype in ['float64', 'float32']:
            df[col] = df[col].round(8)

    excel_filename = 'topology_characteristics.xlsx'
    df.to_excel(excel_filename, index=False)
    print(f"\nРезультати збережено у файл: {excel_filename}")

    total_nodes = topology.adjacency_matrix.shape[0]
    np.random.seed(42)
    data_splits = [np.random.rand(10) for _ in range(total_nodes)]

    gradient_descent = GradientDescent(topology.adjacency_matrix, data_splits)
    final_params = gradient_descent.run()

    print("\nФінальні Параметри:")
    for i, param in enumerate(final_params):
        print(f"Вузол {i + 1}: {param:.4f}")


if __name__ == "__main__":
    main()
