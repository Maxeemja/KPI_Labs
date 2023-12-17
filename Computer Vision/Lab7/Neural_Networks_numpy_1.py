#-------- Приклад "сирої" реалізації нейромережі на рівні 1 присептрона із 3 входами -------------

'''
Приклад побудова елементарної штучної нейронної мережі у сирому коді з numpy
простий персептрон з показовою функцією.

Для синтезу багатошарової нейронної мережі слід реалізувати конкретні кроки:
- опис масиву вхідних даних (навчальних пар) - які визначають склад мережі:
        кількість входів - горизонтальні шари;
        кількість прихованих шарів - агригаторів знань;
- опис алгебри взаємодії прошарків - матричні операції вагового множення;
- опис алгориму навчання;
- навчання;
- прогнозування.

Реалізація зазначених додаткових процесесів реалізовано на рівні numpy операцій в прикладі Neural_Networks_numpy_2.py.
Дані - бінарні зображення літералів - графічі образи;
Технології - не вище функціонального програмування;
Методологічні основи - матричні операції із сирого синтезу нейронних мереж.

Package                      Version
---------------------------- -----------
numpy                        1.23.5

'''

import numpy as np
import matplotlib.pyplot as plt

# 1. Навчальна пара
# вхідні дані абстрактні
inputs = np.array([[0, 1, 0],
                   [0, 1, 1],
                   [0, 0, 0],
                   [1, 0, 0],
                   [1, 1, 1],
                   [1, 0, 1]])
# вихідні дані
outputs = np.array([[0], [0], [0], [1], [1], [1]])

# 2. Конструювання нейрономережі
class NeuralNetwork:
    # ініціалізувати змінні в класі
    def __init__(self, inputs, outputs):
        self.inputs  = inputs
        self.outputs = outputs
        # Вагові коефіціенти
        self.weights = np.array([[0.50], [0.50], [0.50]])
        self.error_history = []
        self.epoch_list = []

    # функція активації показова f(x) = 1 / (1 + e^(-x))
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    # подання вхідних даних до мережі
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    # повернення даних після мережі - похибка
    def backpropagation(self):
        self.error  = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    # тренування мережі на 25 ітераціях (ЕПОХАХ)
    def train(self, epochs=25000):
        for epoch in range(epochs):
            self.feed_forward()
            self.backpropagation()
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    # прогнозовані дані
    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        return prediction

# ініціалізація мережі
NN = NeuralNetwork(inputs, outputs)

# навчання мережі
NN.train()

# приклади результатів тренування
example = np.array([[1, 1, 1]])
example_2 = np.array([[0, 1, 1]])

# відображення результатів
print(NN.predict(example), ' - Correct: ', example[0][0])
print(NN.predict(example_2), ' - Correct: ', example_2[0][0])

# динаміка зміни помилки з часом тренування
plt.figure(figsize=(8, 4))
plt.plot(NN.epoch_list, NN.error_history)
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.show()
