import matplotlib.pyplot as plt
learning_rates = [0.01, 0.1, 0.5, 1]
accuracy = [87, 91, 93, 89]  # Приклад даних

plt.plot(learning_rates, accuracy, marker='o')
plt.title('Залежність точності моделі від швидкості навчання')
plt.xlabel('Швидкість навчання')
plt.ylabel('Точність (%)')
plt.grid()
plt.savefig('accuracy_vs_learning_rate.png')
plt.show()