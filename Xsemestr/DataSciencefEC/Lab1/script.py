import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# 1. Генерація випадкової величини
def generate_random_variable(dist_type, size=1000):
    if dist_type == 'нормальний':
        return np.random.normal(loc=0, scale=1, size=size)
    elif dist_type == 'рівномірний':
        return np.random.uniform(low=-1, high=1, size=size)
    else:
        raise ValueError("Непідтримуваний тип розподілу")


# 2. Генерація тренду
def generate_trend(trend_type, size=1000):
    x = np.linspace(0, 10, size)
    if trend_type == 'лінійний':
        return 2 * x + 5
    elif trend_type == 'квадратичний':
        return 0.5 * x ** 2 + 1.5 * x + 3
    else:
        raise ValueError("Непідтримуваний тип тренду")


# 3. Адитивна модель
def additive_model(trend, noise):
    return trend + noise


# 4. Статистичні характеристики
def calculate_stats(data):
    return {
        'Середнє': np.mean(data),
        'Дисперсія': np.var(data),
        'СКВ': np.std(data)
    }


# 5. Аналіз реальних даних
def analyze_real_data(filepath):
    try:
        df = pd.read_excel(filepath, engine='openpyxl')
        numeric_df = df.apply(pd.to_numeric, errors='coerce')
        return calculate_stats(numeric_df.values.flatten())
    except Exception as e:
        print(f"Помилка читання файлу: {str(e)}")
        return None

# Основна логіка
if __name__ == "__main__":
    # Генерація даних
    noise_normal = generate_random_variable('нормальний')
    noise_uniform = generate_random_variable('рівномірний')

    trend_linear = generate_trend('лінійний')
    trend_quadratic = generate_trend('квадратичний')

    # Комбінації моделей
    combinations = {
        'Лінійний+Нормальний': additive_model(trend_linear, noise_normal),
        'Квадратичний+Рівномірний': additive_model(trend_quadratic, noise_uniform)
    }

    # Аналіз статистик
    for name, data in combinations.items():
        print(f"\n{name} комбінація:")
        stats = calculate_stats(data)
        for k, v in stats.items():
            print(f"{k}: {v:.4f}")

        plt.figure()
        plt.hist(data, bins=30)
        plt.title(f"Гістограма {name}")
        plt.show()

    # Спроба аналізу реальних даних
    real_stats = analyze_real_data('Oschadbank-USD.xls')
    if real_stats:
        print("\nРеальні дані:")
        for k, v in real_stats.items():
            print(f"{k}: {v:.4f}")
