import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import jaccard_score


# ----------------------------------- вхідні дані DataSet масив ------------------------------------
def data_x():
    one = [1, 1, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           1, 1, 1, 1, 1]

    two = [1, 1, 1, 1, 1,
           0, 0, 0, 0, 1,
           1, 1, 1, 1, 1,
           1, 0, 0, 0, 0,
           1, 1, 1, 1, 1]

    three = [1, 1, 1, 1, 1,
             0, 0, 0, 0, 1,
             1, 1, 1, 1, 1,
             0, 0, 0, 0, 1,
             1, 1, 1, 1, 1]

    four = [1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            0, 0, 0, 0, 1]

    five = [1, 1, 1, 1, 1,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            1, 1, 1, 1, 1]

    # ----- Візуалізація --------
    plt.subplot(1, 5, 1)
    plt.imshow(np.array(one).reshape(5, 5))
    plt.subplot(1, 5, 2)
    plt.imshow(np.array(two).reshape(5, 5))
    plt.subplot(1, 5, 3)
    plt.imshow(np.array(three).reshape(5, 5))
    plt.subplot(1, 5, 4)
    plt.imshow(np.array(four).reshape(5, 5))
    plt.subplot(1, 5, 5)
    plt.imshow(np.array(five).reshape(5, 5))
    plt.show()
    # ----- Вхідна частина навчального DataSet масиву --------
    x = [np.array(one).reshape(1, 25), np.array(two).reshape(1, 25),
         np.array(three).reshape(1, 25), np.array(four).reshape(1, 25), np.array(five).reshape(1, 25)]

    return x


def data_y():
    # ----- Вихідна частина навчального DataSet масиву --------
    out = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]]

    y = np.array(out)

    return y


# ----------------------------------- конструювання нейромережі ------------------------------------

# ----- функція активності - сігмоід -----
def sigmoid(x):
    '''
    :param x: - np.array DataSet in
    :return: activation function - sigmoid
    '''

    return (1 / (1 + np.exp(-x)))


# ----- конструювання нейронної мережі  -----
def f_forward(x, w1, w2):
    # структуру вхідного прошарку визначає простір вхідних параметрів x

    # прихований прошарок
    z1 = x.dot(w1)  # зважені вхідні параметри вхідного прошарку 1
    a1 = sigmoid(z1)  # аддитивна згортка - вихід з прошарку 1 - вхід прошарку 2

    # вихідний прошарок
    z2 = a1.dot(w2)  # зважені вхідні параметри прошарку 2 на вихідний прошарок
    a2 = sigmoid(z2)  # вихідні параметри нейромережі

    return (a2)


# ------- ініціалізація початкових значення вагових коефіціентів мережі методом рандомізації
def generate_wt(x, y):
    l = []
    for i in range(x * y):
        l.append(np.random.randn())
    return (np.array(l).reshape(x, y))


# ------- контроль навченості мережі за середньоквадратичною помилкою mean square error(MSE)
def loss(out, Y):
    s = (np.square(out - Y))
    s = np.sum(s) / len(y)
    return (s)


# ------- зворотне поширення помилки -------------------------------------------------------
def back_prop(x, y, w1, w2, alpha):
    # прихований прошарок
    z1 = x.dot(w1)  # зважені вхідні параметри вхідного прошарку 1
    a1 = sigmoid(z1)  # аддитивна згортка - вихід з прошарку 1 - вхід прошарку 2

    # вихідний прошарок
    z2 = a1.dot(w2)  # зважені вхідні параметри прошарку 2 на вихідний прошарок
    a2 = sigmoid(z2)  # вихідні параметри нейромережі

    # похибка на вихідному прошарку
    d2 = (a2 - y)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(),
                     (np.multiply(a1, 1 - a1)))

    w1_adj = x.transpose().dot(d1)
    w2_adj = a1.transpose().dot(d2)

    # оновлення параметрів з контролем помилки alpha
    w1 = w1 - (alpha * (w1_adj))
    w2 = w2 - (alpha * (w2_adj))

    return (w1, w2)


# ------- тренування мережі з контролем помилки alpha на epoch -----------------------------
def train(x, Y, w1, w2, alpha=0.01, epoch=10):
    acc = []
    losss = []
    for j in range(epoch):
        l = []
        for i in range(len(x)):
            out = f_forward(x[i], w1, w2)
            l.append((loss(out, Y[i])))
            w1, w2 = back_prop(x[i], y[i], w1, w2, alpha)
        print("epochs:", j + 1, "======== acc:", (1 - (sum(l) / len(x))) * 100)
        acc.append((1 - (sum(l) / len(x))) * 100)
        losss.append(sum(l) / len(x))
    return (acc, losss, w1, w2)


# ------- ідентифікація літералів / передбачення ------------------------------------------
def predict(x, w1, w2):
    Out = f_forward(x, w1, w2)
    maxm = 0
    k = 0
    for i in range(len(Out[0])):
        if (maxm < Out[0][i]):
            maxm = Out[0][i]
            k = i
    if (k == 0):
        print("Image of one", '\n')
    elif (k == 1):
        print("Image of two", '\n')
    elif (k == 2):
        print("Image of three", '\n')
    elif (k == 3):
        print("Image of four", '\n')
    else:
        print("Image of five", '\n')
    plt.imshow(x.reshape(5, 5))
    plt.show()

    return Out


# ------------------------------- БЛОК ГОЛОВНИХ ВИКЛИКІВ -------------------------------------------------------
if __name__ == '__main__':

    # ------------------- вхідні дані -----------------------------------
    x = data_x()
    y = data_y()
    print('DataSet-масив: навчальна пара для навчання із вчителем')
    print('х = ', x, '\n')
    print('y = ', y, '\n')

    # --- ініціалізація вагових коєфіцієнтів на 2 прошарка з відповідним до характеристик прошарків складом параметрів
    w1 = generate_wt(25, 5)
    w2 = generate_wt(5, 5)
    print('ініціалізація вагових коєфіцієнтів на 2 прошарка')
    print('(w1 = ', w1, '\n')
    print('w2 = ', w2, '\n')

    # ------- тренування мережі з контролем помилки alpha на epoch -------
    print('тренування мережі з контролем помилки alpha на epoch')
    acc, losss, w1, w2 = train(x, y, w1, w2, 0.1, 100)

    # натреновані вагови коефіцієнти
    print('натреновані вагови коефіцієнти  на 2 прошарка')
    print('(w1 = ', w1, '\n')
    print('w2 = ', w2, '\n')

    # -------------- контроль / візуалізація параметрів тренування -------
    # точність
    plt.plot(acc)
    plt.ylabel('Точність')
    plt.xlabel("Епохи:")
    plt.show()
    # втрати
    plt.plot(losss)
    plt.ylabel('Втрати')
    plt.xlabel("Епохи:")
    plt.show()

    one_test = [1, 1, 1, 0, 0,
                0, 0, 1, 0, 0,
                0, 1, 1, 0, 0,
                0, 0, 1, 0, 0,
                1, 1, 1, 1, 1]

    two_test = [1, 1, 1, 1, 0,
                0, 0, 0, 0, 1,
                1, 1, 1, 1, 1,
                1, 0, 0, 0, 0,
                1, 1, 1, 1, 1]

    three_test = [1, 1, 1, 1, 0,
                  0, 0, 0, 0, 1,
                  1, 1, 1, 1, 1,
                  0, 0, 0, 0, 1,
                  1, 1, 1, 1, 1]

    four_test = [1, 1, 0, 0, 1,
                 1, 0, 0, 0, 1,
                 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 1,
                 0, 0, 0, 0, 1]

    five_test = [1, 1, 1, 1, 0,
                 1, 0, 0, 0, 0,
                 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 1,
                 1, 1, 1, 1, 1]

    test_data_x = [np.array(one_test).reshape(1, 25), np.array(two_test).reshape(1, 25),
                   np.array(three_test).reshape(1, 25), np.array(four_test).reshape(1, 25),
                   np.array(five_test).reshape(1, 25)]

    jaccard_similarities = []
    symbols = ["1", "2", "3", "4", "5"]

    for i in range(len(test_data_x)):
        print(f'Вхідні параметри відповідають символу {symbols[i]}')
        print('Результат ідентифікації:')
        predicted_output = predict(test_data_x[i], w1, w2)

        # Змінити форму predicted_output відповідно до форми y[i]
        predicted_output = predicted_output.reshape(y[i].shape)

        y_binary = np.round(y[i])
        predicted_binary = np.round(predicted_output)

        # Розрахунок схожості
        jaccard_similarity = jaccard_score(y_binary, predicted_binary, average='micro')
        jaccard_similarities.append(jaccard_similarity)

        print(f'Точність: {jaccard_similarity:.2f}\n')

    # Середня схожість між всіма передбаченнями
    average_jaccard_similarity = sum(jaccard_similarities) / len(jaccard_similarities)
    print(f'Середня точність: {average_jaccard_similarity:.2f}')
