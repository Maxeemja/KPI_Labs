import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns


# =============================================
# 1. Генерація синтетичних даних для навчання
# =============================================
def generate_data(num_samples=1000, img_size=8, num_classes=10):
    """
    Генерує синтетичні бінарні зображення символів (8x8 пікселів)
    та відповідні мітки класів з шумом для імітації реальних даних
    """
    X = []
    y = []
    np.random.seed(42)

    for _ in range(num_samples):
        # Генерація бінарної матриці з шумом
        img = np.random.choice([0, 1], size=(img_size, img_size), p=[0.2, 0.8])
        # Додавання шуму
        noise = np.random.choice([0, 1], size=(img_size, img_size), p=[0.95, 0.05])
        img = np.logical_xor(img, noise).astype(int)

        # Генерація міток
        label = np.random.randint(0, num_classes)
        X.append(img.flatten())
        y.append(label)

    # Перетворення в one-hot encoding
    y_onehot = np.eye(num_classes)[y]
    return np.array(X).T, np.array(y).reshape(1, -1), y_onehot.T


# =============================================
# 2. Клас нейронної мережі
# =============================================
class NeuralNetwork:
    def __init__(self, layer_dims, learning_rate=0.1):
        self.params = {}
        self.learning_rate = learning_rate

        # Ініціалізація ваг та зміщень
        np.random.seed(42)
        for l in range(1, len(layer_dims)):
            self.params[f'W{l}'] = np.random.randn(layer_dims[l], layer_dims[l - 1]) * 0.01
            self.params[f'b{l}'] = np.zeros((layer_dims[l], 1))

    def relu(self, Z):
        return np.maximum(0, Z)

    def softmax(self, Z):
        exp = np.exp(Z - np.max(Z))
        return exp / exp.sum(axis=0, keepdims=True)

    def forward(self, X):
        cache = {'A0': X}
        L = len(self.params) // 2

        for l in range(1, L):
            cache[f'Z{l}'] = np.dot(self.params[f'W{l}'], cache[f'A{l - 1}']) + self.params[f'b{l}']
            cache[f'A{l}'] = self.relu(cache[f'Z{l}'])

        # Вихідний шар з softmax
        cache[f'Z{L}'] = np.dot(self.params[f'W{L}'], cache[f'A{L - 1}']) + self.params[f'b{L}']
        cache[f'A{L}'] = self.softmax(cache[f'Z{L}'])
        return cache

    def compute_loss(self, AL, Y):
        m = Y.shape[1]
        return -np.sum(Y * np.log(AL + 1e-8)) / m

    def backward(self, cache, X, Y):
        gradients = {}
        m = X.shape[1]
        L = len(self.params) // 2

        # Градієнти вихідного шару
        dZ = cache[f'A{L}'] - Y
        gradients[f'dW{L}'] = np.dot(dZ, cache[f'A{L - 1}'].T) / m
        gradients[f'db{L}'] = np.sum(dZ, axis=1, keepdims=True) / m

        # Зворотне поширення для прихованих шарів
        for l in reversed(range(1, L)):
            dA_prev = np.dot(self.params[f'W{l + 1}'].T, dZ)
            dZ = dA_prev * (cache[f'Z{l}'] > 0).astype(float)
            gradients[f'dW{l}'] = np.dot(dZ, cache[f'A{l - 1}'].T) / m
            gradients[f'db{l}'] = np.sum(dZ, axis=1, keepdims=True) / m

        return gradients

    def update_params(self, gradients):
        for key in self.params:
            self.params[key] -= self.learning_rate * gradients[f'd{key}']


# =============================================
# 3. Навчання моделі
# =============================================
# Генерація даних
X_train, y_train, y_train_onehot = generate_data(num_samples=5000, num_classes=10)
X_test, y_test, y_test_onehot = generate_data(num_samples=1000, num_classes=10)

# Архітектура мережі: 64-128-64-10
layer_dims = [64, 128, 64, 10]
nn = NeuralNetwork(layer_dims, learning_rate=0.1)

# Навчання
epochs = 200
batch_size = 64
loss_history = []
accuracy_history = []

for epoch in range(epochs):
    epoch_loss = 0
    for i in range(0, X_train.shape[1], batch_size):
        # Вибір батчу
        X_batch = X_train[:, i:i + batch_size]
        y_batch = y_train_onehot[:, i:i + batch_size]

        # Пряме та зворотне поширення
        cache = nn.forward(X_batch)
        loss = nn.compute_loss(cache[f'A{len(layer_dims) - 1}'], y_batch)
        gradients = nn.backward(cache, X_batch, y_batch)
        nn.update_params(gradients)

        epoch_loss += loss

    # Обчислення точності
    cache_test = nn.forward(X_test)
    AL = cache_test[f'A{len(layer_dims) - 1}']
    predictions = np.argmax(AL, axis=0)
    accuracy = np.mean(predictions == y_test.flatten())

    loss_history.append(epoch_loss / (X_train.shape[1] / batch_size))
    accuracy_history.append(accuracy)

    print(f"Epoch {epoch + 1}/{epochs} | Loss: {loss_history[-1]:.4f} | Accuracy: {accuracy:.4f}")

# =============================================
# 4. Візуалізація результатів
# =============================================
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(loss_history)
plt.title('Функція втрат')
plt.xlabel('Епоха')
plt.ylabel('Loss')

plt.subplot(1, 2, 2)
plt.plot(accuracy_history)
plt.title('Точність на тестовому наборі')
plt.xlabel('Епоха')
plt.ylabel('Accuracy')
plt.show()

# Матриця плутанини
cache_final = nn.forward(X_test)
predictions = np.argmax(cache_final[f'A{len(layer_dims) - 1}'], axis=0)
cm = confusion_matrix(y_test.flatten(), predictions)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Матриця плутанини')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

print(classification_report(y_test.flatten(), predictions))
