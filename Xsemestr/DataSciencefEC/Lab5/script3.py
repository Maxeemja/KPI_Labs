import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    """Обчислює гістограму зображення."""
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                        [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

def compare_images(image_path1, image_path2):
    """Порівнює два зображення за допомогою порівняння гістограм."""
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    if img1 is None or img2 is None:
        raise ValueError("Не вдалося завантажити одне або обидва зображення.")

    hist1 = calculate_histogram(img1)
    hist2 = calculate_histogram(img2)

    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return similarity

# Шляхи до зображень
image_path1 = 'image.jpg'
image_path2 = 'image.jpg'

try:
    similarity_score = compare_images(image_path1, image_path2)
    print(f"Показник схожості: {similarity_score}")

    # Відображення зображень
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title('Зображення 1')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.title('Зображення 2')
    plt.axis('off')

    plt.show()

except ValueError as e:
    print(f"Помилка: {e}")
except Exception as e:
    print(f"Неочікувана помилка: {e}")
