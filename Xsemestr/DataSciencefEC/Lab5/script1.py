from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Генерація модельних даних
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Навчання моделі k-means
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

# Візуалізація
plt.scatter(X[:,0], X[:,1], c=labels)
plt.scatter(centroids[:,0], centroids[:,1], marker='X', s=200, c='red')
plt.title('Кластеризація методом k-means')
plt.show()
