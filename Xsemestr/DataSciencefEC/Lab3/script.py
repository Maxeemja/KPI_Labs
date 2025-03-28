import numpy as np

# Функція для нормалізації матриці
def normalize_matrix(matrix):
    col_sums = matrix.sum(axis=0)
    return matrix / col_sums

# Функція для обчислення ваг критеріїв
def calculate_criteria_weights(normalized_matrix):
    return normalized_matrix.mean(axis=1)

# Функція для перевірки узгодженості матриці
def consistency_ratio(matrix, weights):
    n = matrix.shape[0]
    lambda_max = np.sum(np.dot(matrix, weights) / weights) / n
    ci = (lambda_max - n) / (n - 1)
    random_index = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41}
    ri = random_index.get(n, 1.41)
    cr = ci / ri if ri != 0 else 0
    return cr

# Дані: матриця парних порівнянь критеріїв
criteria_matrix = np.array([
    [1,   3,   7],   # Наприклад: Відсоткова ставка, Надійність банку, Додаткові умови
    [1/3, 1,   5],
    [1/7, 1/5, 1]
])

# Нормалізація матриці критеріїв
normalized_criteria_matrix = normalize_matrix(criteria_matrix)

# Розрахунок ваг критеріїв
criteria_weights = calculate_criteria_weights(normalized_criteria_matrix)

# Перевірка узгодженості
cr = consistency_ratio(criteria_matrix, criteria_weights)
if cr < 0.10:
    print("Матриця узгоджена.")
else:
    print("Матриця не узгоджена! CR =", cr)

print("Ваги критеріїв:", criteria_weights)

# Дані: матриця альтернатив (банківських пропозицій)
alternatives_matrix = np.array([
    [4.5, 8,   6],   # Альтернатива A (банк A)
    [3.8, 9,   5],   # Альтернатива B (банк B)
    [4.2, 7.5, 7]    # Альтернатива C (банк C)
])

# Нормалізація альтернатив за кожним критерієм
normalized_alternatives_matrix = normalize_matrix(alternatives_matrix)

# Розрахунок зважених оцінок альтернатив
weighted_scores = normalized_alternatives_matrix @ criteria_weights

# Вибір найкращої альтернативи
best_alternative_index = np.argmax(weighted_scores)
print("Найкраща альтернатива:", f"Альтернатива {chr(65 + best_alternative_index)}")
print("Оцінки альтернатив:", weighted_scores)
