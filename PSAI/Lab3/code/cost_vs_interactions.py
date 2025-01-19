import matplotlib.pyplot as plt

iterations = [100, 200, 300, 400, 500]
cost_values = [0.693, 0.583, 0.482, 0.391, 0.312]  # Приклад даних

plt.plot(iterations, cost_values, marker='o')
plt.title('Залежність значення цільової функції від кількості ітерацій')
plt.xlabel('Кількість ітерацій')
plt.ylabel('Значення цільової функції')
plt.grid()
plt.savefig('cost_vs_iterations.png')
plt.show()
