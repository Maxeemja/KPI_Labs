from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Покращення контрасту
image = Image.open('image.jpg')
enhancer = ImageEnhance.Contrast(image)
image_enhanced = enhancer.enhance(2.0)  # Збільшення контрасту на 200%[6]

# Перетворення зображення у масив пікселів
pixels = np.array(image_enhanced).reshape(-1, 3)

# Кластеризація кольорів методом k-means
kmeans = KMeans(n_clusters=5)
kmeans.fit(pixels)
dominant_colors = kmeans.cluster_centers_.astype(int)

# Відображення домінантних кольорів
plt.figure(figsize=(10,2))
for i, color in enumerate(dominant_colors):
    plt.fill_between([i, i+1], 0, 1, color=color/255)
plt.axis('off')
plt.title('Домінантні кольори (k=5)')
plt.show()
