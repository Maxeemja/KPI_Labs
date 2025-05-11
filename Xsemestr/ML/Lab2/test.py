import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
np.random.seed(123)

digits = load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y)
print(f'X_train shape: {X_train.shape}')
print(f'y_train shape: {y_train.shape}')
print(f'X_test shape: {X_test.shape}')
print(f'y_test shape: {y_test.shape}')

# Приклад цифр
fig = plt.figure(figsize=(10,8))
for i in range(10):
    ax = fig.add_subplot(2, 5, i+1)
    plt.imshow(X[i].reshape((8,8)), cmap='gray')

plt.show()



class kNN():
  def __init__(self):
    pass

  def fit(self, X, y):
    self.data = X
    self.targets = y

  def euclidean_distance(self, X):
    """
    Обчислює евклідову відстань між навчальними даними та
    новим вхідним прикладом або матрицею вхідних прикладів X
    """
    # вхід: один приклад
    if X.ndim == 1:
      # BEGIN_YOUR_CODE
      l2 = np.sqrt(np.sum((self.data - X) ** 2, axis=1))
      # END_YOUR_CODE

    # вхід: кілька прикладів (матриця)
    if X.ndim == 2:
      n_samples, _ = X.shape
      # BEGIN_YOUR_CODE
      l2 = np.zeros((n_samples, len(self.data)))
      for i in range(n_samples):
        l2[i] = np.sqrt(np.sum((self.data - X[i]) ** 2, axis=1))
      # END_YOUR_CODE

    return np.array(l2)

  def predict(self, X, k=1):
    """
    Прогноз класу для вхідного прикладу або матриці вхідних прикладів X
    """
    # крок 1: обчислення відстані між вхідними та навчальними даними
    dists = self.euclidean_distance(X)

    # крок 2: знайти k найближчих сусідів та їх категорію (клас)
    if X.ndim == 1:
      if k == 1:
        # BEGIN_YOUR_CODE
        nn = np.argmin(dists)  # індекс найближчого сусіда
        return self.targets[nn]
        # END_YOUR_CODE
      else:
        # BEGIN_YOUR_CODE
        knn = np.argsort(dists)[:k]  # індекси k найближчих сусідів
        y_knn = self.targets[knn]    # класи k найближчих сусідів

        # підрахунок голосів (найчастіший клас)
        unique_classes = np.unique(self.targets)
        votes = np.zeros(len(unique_classes))

        for i, cls in enumerate(unique_classes):
            votes[i] = np.sum(y_knn == cls)

        return unique_classes[np.argmax(votes)]
        # END_YOUR_CODE

    if X.ndim == 2:
      knn = np.argsort(dists)[:, :k]
      y_knn = self.targets[knn]
      if k == 1:
        # BEGIN_YOUR_CODE
        # Повертаємо масив класів найближчих сусідів для кожного вхідного прикладу
        return np.array([self.targets[np.argmin(dists[i])] for i in range(len(dists))])
        # END_YOUR_CODE
      else:
        # BEGIN_YOUR_CODE
        # голосування для кожного вхідного прикладу
        n_samples = X.shape[0]
        y_pred = np.zeros(n_samples, dtype=self.targets.dtype)
        unique_classes = np.unique(self.targets)

        for i in range(n_samples):
            votes = np.zeros(len(unique_classes))

            for j, cls in enumerate(unique_classes):
                votes[j] = np.sum(y_knn[i] == cls)

            y_pred[i] = unique_classes[np.argmax(votes)]

        return y_pred
        # END_YOUR_CODE



knn = kNN()
knn.fit(X_train, y_train)

print("Тестування для одного вхідного прикладу, k=1")
print(f"Передбачена мітка: {knn.predict(X_test[0], k=1)}")
print(f"Істинна мітка: {y_test[0]}")
print()
print("Тестування для одного вхідного прикладу, k=5")
print(f"Передбачена мітка: {knn.predict(X_test[40], k=5)}")
print(f"Істинна мітка: {y_test[40]}")
print()
print("Тестування для 10 вхідних прикладів, k=1")
print(f"Передбачені мітки: {knn.predict(X_test[10:20], k=1)}")
print(f"Істинна мітка: {y_test[10:20]}")
print()
print("Тестування для 10 вхідних прикладів, k=4")
print(f"Передбачена мітка: {knn.predict(X_test[10:20], k=6)}")
print(f"Істинна мітка: {y_test[10:20]}")
print()

# Compute accuracy on test set
y_p_test1 = knn.predict(X_test, k=1)
test_acc1 = np.sum(y_p_test1[0] == y_test)/len(y_p_test1[0]) * 100
print(f"Test accuracy with k = 1: {format(test_acc1)}")

y_p_test5 = knn.predict(X_test, k=3)
test_acc5= np.sum(y_p_test5 == y_test)/len(y_p_test5) * 100
print(f"Test accuracy with k = 5: {format(test_acc5)}")