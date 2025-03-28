import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys


# ------------------------ Завантаження та очищення даних --------------------------
def load_and_clean_data(file_name, column_name):
    # Завантаження даних із файлу Excel
    data = pd.read_excel(file_name)

    # Вибір потрібної колонки
    if column_name not in data.columns:
        raise ValueError(f"Колонка '{column_name}' не знайдена у файлі.")

    raw_data = data[column_name]

    # Перетворення на числові значення, некоректні значення замінюються на NaN
    numeric_data = pd.to_numeric(raw_data, errors='coerce')

    # Заповнення NaN значеннями середнім значенням по вибірці
    cleaned_data = numeric_data.fillna(numeric_data.mean())

    return cleaned_data.values


# ------------------------ Детекція аномалій (метод IQR) --------------------------
def detect_anomalies_iqr(data, threshold=1.5):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1

    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR

    filtered_data = np.clip(data, lower_bound, upper_bound)
    return filtered_data


# ------------------------ Поліноміальна регресія --------------------------
def polynomial_regression(data, degree=2):
    x = np.arange(len(data))
    coeffs = np.polyfit(x, data, degree)
    poly_model = np.poly1d(coeffs)
    return poly_model, coeffs


# ------------------------ Прогнозування --------------------------
def extrapolate(model, n_future):
    n_current = len(model)
    x_future = np.arange(n_current, n_current + n_future)
    y_future = model(x_future)
    return y_future


# ------------------------ Альфа-бета фільтр --------------------------
def alpha_beta_filter(data, alpha=0.7, beta=0.2):
    filtered_data = []
    x_estimate = data[0]
    velocity_estimate = 0

    for measurement in data:
        # Prediction step
        x_predict = x_estimate + velocity_estimate

        # Update step
        residual = measurement - x_predict
        x_estimate = x_predict + alpha * residual
        velocity_estimate = velocity_estimate + beta * residual

        filtered_data.append(x_estimate)

    return filtered_data


# ------------------------ Оцінка якості моделі (R^2) --------------------------
def calculate_r_squared(data, model):
    y_predicted = model(np.arange(len(data)))
    ss_res = np.sum((data - y_predicted) ** 2)
    ss_tot = np.sum((data - np.mean(data)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared


# ------------------------ Основний скрипт --------------------------
if __name__ == "__main__":
    # Параметри
    file_name = "Oschadbank-USD.xls"  # Змінити на реальне ім'я файлу
    column_name = "КурсНбу"  # Назва колонки з даними
    future_interval_ratio = 0.5  # Прогнозування на 50% інтервалу

    # Завантаження та очищення даних
    try:
        clean_data = load_and_clean_data(file_name, column_name)
    except Exception as e:
        print(f"Помилка при завантаженні та очищенні даних: {e}")
        sys.exit()

    # Детекція та обробка аномалій
    filtered_data = detect_anomalies_iqr(clean_data)

    # 1. Група вимог_1: Поліноміальна регресія
    poly_model, coeffs = polynomial_regression(filtered_data)
    print("\nГрупа вимог_1: Поліноміальна регресія")
    print("Поліноміальна модель:", poly_model)

    # Обчислення R^2 для поліноміальної моделі
    r_squared_poly = calculate_r_squared(filtered_data, poly_model)
    print(f"Коефіцієнт детермінації R^2 для поліноміальної регресії: {r_squared_poly}")

    # Прогнозування
    n_future = int(len(filtered_data) * future_interval_ratio)
    future_predictions = extrapolate(poly_model, n_future)

    # 2. Група вимог_2: Альфа-бета фільтр
    # Адаптація параметрів альфа-бета фільтра на основі R^2
    if r_squared_poly > 0.8:
        alpha = 0.8
        beta = 0.1
        print(
            "\nВисока якість моделі (R^2 > 0.8): Використовуємо параметри альфа-бета фільтра для меншого згладжування.")
    else:
        alpha = 0.3
        beta = 0.05
        print(
            "\nНизька якість моделі (R^2 <= 0.8): Використовуємо параметри альфа-бета фільтра для сильнішого згладжування.")

    smoothed_data = alpha_beta_filter(filtered_data, alpha, beta)
    print("\nГрупа вимог_2: Альфа-бета фільтр")

    # Візуалізація результатів
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_data, label="Очищені дані (IQR)")
    plt.plot(smoothed_data, label="Згладжені дані (Альфа-бета фільтр)")

    # Відображення прогнозованих значень
    future_x = np.arange(len(filtered_data), len(filtered_data) + n_future)
    plt.plot(future_x, future_predictions, label="Прогноз (Поліноміальна регресія)")

    plt.xlabel("Час")
    plt.ylabel("Значення")
    plt.title("Аналіз та прогнозування даних")
    plt.legend()
    plt.grid(True)
    plt.show()
