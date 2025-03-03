# Імпортуємо необхідні бібліотеки
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Завантаження даних
train = pd.read_csv('/kaggle/input/linear-regression-2025/train.csv')  
test = pd.read_csv('/kaggle/input/linear-regression-2025/test.csv')

# Попередня обробка даних
# Вибираємо вхідні ознаки (features) та цільову змінну (target)
X_train = train[['mpg', 'cylinders', 'displacement', 'weight', 'horsepower']]
y_train = train['acceleration']

X_test = test[['mpg', 'cylinders', 'displacement', 'weight', 'horsepower']]

# Перевіряємо наявність пропущених значень
if X_train.isnull().sum().any() or X_test.isnull().sum().any():
    print("Пропущені значення знайдено, заповнюємо їх середнім...")
    X_train.fillna(X_train.mean(), inplace=True)
    X_test.fillna(X_test.mean(), inplace=True)

# Стандартизація даних (масштабування)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Створення та навчання моделі лінійної регресії
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Передбачення на тестовій вибірці
predictions = model.predict(X_test_scaled)

# Формування результату у потрібному форматі
submission = pd.DataFrame({
    'ID': test['ID'],
    'acceleration': predictions
})

# Збереження у CSV файл для сабміту
submission.to_csv('submission.csv', index=False)
print("Файл submission.csv створено!")
