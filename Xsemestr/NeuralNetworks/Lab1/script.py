import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Завантаження тренувального та тестового наборів даних
train = pd.read_csv('/kaggle/input/mnist-nn-2025/train.csv')
test = pd.read_csv('/kaggle/input/mnist-nn-2025/test.csv')

# Розділення тренувальних даних на ознаки (X) та мітки (y)
X_train = train.iloc[:, 2:].values  # Всі стовпці, починаючи з другого (пікселі)
y_train = train.iloc[:, 1].values   # Другий стовпець - мітки

# Перевірка форми X_train перед reshape
print(f"X_train shape before reshape: {X_train.shape}")

# Зміна форми X_train у формат (n, 28, 28)
try:
    X_train = X_train.reshape(-1, 28, 28) / 255.0
    print(f"X_train shape after reshape: {X_train.shape}")
except ValueError as e:
    print(f"Помилка при зміні форми: {e}")
    raise

# One-hot encoding для міток y_train
y_train = to_categorical(y_train)

# Обробка тестових даних
X_test = test.iloc[:, 1:].values  # Всі стовпці, починаючи з другого (пікселі)
print(f"X_test shape before reshape: {X_test.shape}")

try:
    X_test = X_test.reshape(-1, 28, 28) / 255.0
    print(f"X_test shape after reshape: {X_test.shape}")
except ValueError as e:
    print(f"Помилка при зміні форми X_test: {e}")
    raise

# Побудова моделі MLP
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Компіляція моделі
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Навчання моделі
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Прогнозування на тестових даних
predictions = model.predict(X_test)
predicted_labels = np.argmax(predictions, axis=1)

# Збереження результатів у CSV-файл у форматі Kaggle Submission
submission = pd.DataFrame({'Id': test['Id'], 'label': predicted_labels})
submission.to_csv('/kaggle/working/submission.csv', index=False)

print("Скрипт завершено. Результати збережено у submission.csv.")
