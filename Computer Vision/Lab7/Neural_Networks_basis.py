
'''
Приклад побудова елементарної штучної нейронної мережі у сирому коді з numpy
простий персептрон з показовою функцією

Package                      Version
---------------------------- -----------
numpy                        1.23.5

'''

import numpy as np

# 1. Побудова простого нейрону: функція активації показова f(x) = 1 / (1 + e^(-x))
def sigmoid(x):
     return 1 / (1 + np.exp(-x))
# 2. Синтез ростого персептрона з показовою функцією
class Neuron:
   def __init__(self, weights, bias): # Параметри
        self.weights = weights
        self.bias = bias
   def feedforward(self, inputs):     # Обрахунки
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
# 3. Ініціалізація процесів синтезу нейрона
weights = np.array([0, 1])            # w1 = 0, w2 = 1
bias = 4                              # b = 4
n = Neuron(weights, bias)
x = np.array([2, 3])                  # x1 = 2, x2 = 3
print(n.feedforward(x))               # 0.9990889488055994
