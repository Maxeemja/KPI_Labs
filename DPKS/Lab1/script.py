import numpy as np

matrix = [
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0]
]


def Diameter(MA):
    max_val = np.max(MA)
    return max_val


def Degree(MA):
    return np.max([np.sum(A) for A in MA])


def AverageDiameter(MA):
    return np.sum(MA) / (len(MA) * (len(MA) - 1))


def Cost(MA, MD):
    return len(MA) * Diameter(MD) * Degree(MA)


def ToDistanceMatrix(MA):
    distance = np.matrix(MA)
    for i in range(len(MA)):
        for j in range(len(MA)):
            if distance[i, j] == 0:
                distance[i, j] = 9000000
    for k in range(len(MA)):
        for i in range(len(MA)):
            for j in range(len(MA)):
                if distance[i, j] > distance[i, k] + distance[k, j]:
                    distance[i, j] = distance[i, k] + distance[k, j]
    for i in range(len(MA)):
        distance[i, i] = 0
    for j in range(len(MA)):
        distance[j, i] = distance[i, j]
    return distance


def Traffic(MA, MD):
    return (2 * AverageDiameter(MD)) / Degree(MA)


def circle_cluster(step):
    N = 10
    new_cluster = np.zeros(shape=(N * step, N * step), dtype=int)

    for i in range(0, step):
        for j in range(0, N):
            for k in range(0, N):
                new_cluster[N * i + j, N * i + k] = matrix[j][k]
        if i >= 1:
            new_cluster[N * i - 2, N * i + 0] = 1
            new_cluster[N * i - 1, N * i + 1] = 1
            new_cluster[N * i + 0, N * i - 2] = 1
            new_cluster[N * i + 1, N * i - 1] = 1
        # Додавання нерегулярних зв'язків лише для непарних кластерів
        if (i % 2) != 0:
            for j in range(N):
                new_cluster[N * i + j, N * (i - 1) + j] = 1
                new_cluster[N * (i - 1) + j, N * i + j] = 1

    if step > 1:
        new_cluster[0, N * step - 2] = 1
        new_cluster[1, N * step - 1] = 1
        new_cluster[N * step - 2, 0] = 1
        new_cluster[N * step - 1, 1] = 1

    return new_cluster


if __name__ == "__main__":
    print("     Step     Nodes          Diameter            Degree       Av.Diameter     Cost      Traffic")
    for step in range(1, 16):
        cluster = circle_cluster(step)
        dist = ToDistanceMatrix(cluster)
        D = Diameter(dist)
        S = Degree(cluster)
        AvgD = AverageDiameter(dist)
        C = Cost(cluster, dist)
        T = Traffic(cluster, dist)
        print("{:10} {:10}    {:10}    {:15}    {:10.4f}    {:10}    {:10.4f}"
              .format(step, step * 10, D, S, AvgD, C, T))
