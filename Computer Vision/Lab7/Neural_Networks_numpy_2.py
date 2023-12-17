# ------------------- Приклад "сирої" реалізації нейромережі  --------------------------

'''
Приклад побудова елементарної штучної нейронної мережі з характеристиками:

https://www.geeksforgeeks.org/implementation-of-neural-network-from-scratch-using-numpy/
https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65
https://medium.com/@waleedmousa975/building-a-neural-network-from-scratch-using-numpy-and-math-libraries-a-step-by-step-tutorial-in-608090c20466
https://levelup.gitconnected.com/coding-a-deep-neural-network-from-scratch-17bbc507e7c0
https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65
https://towardsdatascience.com/coding-a-neural-network-from-scratch-in-numpy-31f04e4d605



1. Кількість входів  30 (вхідних - горизонтальних прошарків) - 30 координат в кодуванні зображення одного літерала;
2. Кількість виходів 3 (вихідних - горизонтальних прошарків) - кількість екземплярів літерала для ідентифікації - 3.
3. 30 входів - згортаються до 3 виходів за аддитивною згорткою пресиптрона в схемі вагового згортання.
4. Згортання на прикладі графічних образім пояснює термін "згорткової нейронної мережі" - що застосовується для обробки зображень.
5. Вертикальна архітектура нейромережі:
    1-й рівень: вхідний рівень (1, 30)
    2-й шар: прихований шар (1, 5)
    3-й шар: вихідний рівень (3, 3)

Для синтезу багатошарової нейронної мережі реалізовано кроки:
- опис масиву вхідних даних (навчальних пар) - які визначають склад мережі:
        кількість входів - горизонтальні шари;
        кількість прихованих шарів - агригаторів знань;
- опис алгебри взаємодії прошарків - матричні операції вагового множення;
- опис алгориму навчання;
- навчання;
- ідентифікація / прогнозування.

Дані - бінарні зображення літералів - графічі образи - літерали;
Технології - не вище функціонального програмування;
Методологічні основи - матричні операції із сирого синтезу нейронних мереж.

Package                      Version
---------------------------- -----------
numpy                        1.23.5

'''

import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------- вхідні дані DataSet масив ------------------------------------
def data_x():
    '''
    Вхідна частина навчального DataSet масиву
    формування вхідних бінарних даних графічних примітивів
    :return: x - np.array
    '''

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
    x = [np.array(one).reshape(1, 25),
         np.array(two).reshape(1, 25),
         np.array(three).reshape(1, 25),
         np.array(four).reshape(1, 25),
         np.array(five).reshape(1, 25)]

    return x


def data_y():
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
    '''
    Головна компонента конструювання нейронної мережі.
    Цим та подальшими відрізняється цей приклад від звичайного пресептрона
    Архітектурні залежності:
    1-й рівень: вхідний рівень (1, 30);
    2-й шар: прихований шар (1, 5);
    3-й шар: вихідний рівень (3, 3).
    Графічне відображення архітектури див.Neural_Networks_numpy_2.jpg

    :param x: np.array -
    :param w1: початкові вагові коефіціенти 1 прошарку (вхідного)
    :param w2: початкові вагові коефіціенти 2 прошарку (прихованого)
    :return: a2 - вектор вихідних параметрів мережі - 3 компоненти
    '''

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
    # z2 = w1.dot(w2)
    # out = sigmoid(z2)  # out will now be shape (5,)
    #
    # # RMSE loss
    # s = (np.square(out - Y))
    # s = np.sum(s) / len(Y)
    #
    # return s

    total_loss = 0
    for i in range(len(out)):
        sample_out = out[i]
        label = Y[i]

        loss = np.square(sample_out - label).sum()
        total_loss += loss

    return total_loss / len(out)


# ------- зворотне поширення помилки -------------------------------------------------------
def back_prop(x, y, w1, w2, alpha):
    # прихований прошарок
    z1 = x.dot(w1)  # зважені вхідні параметри вхідного прошарку 1
    a1 = sigmoid(z1)  # аддитивна згортка - вихід з прошарку 1 - вхід прошарку 2

    # вихідний прошарок
    z2 = a1.dot(w2)  # зважені вхідні параметри прошарку 2 на вихідний прошарок
    a2 = sigmoid(z2)  # вихідні параметри нейромережі

    # похибка на вихідному прошарку
    d2_list = []
    for i in range(len(a2)):
        sample_out = a2[i]
        sample_label = y[i]

        d2 = sample_out - sample_label
        d2_list.append(d2)

    d2 = np.array(d2_list)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(),
                     (np.multiply(a1, 1 - a1)))

    # градієнт для w1 і w2
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
    '''
    Функція прогнозу прийматиме такі аргументи:
    :param x: матриця зображення
    :param w1: треновані ваги
    :param w2: треновані ваги
    :return: відображає ідентифікований літерал - графічну формиу
    '''

    Out = f_forward(x, w1, w2)
    maxm = 0
    k = 0
    for i in range(len(Out[0])):
        if (maxm < Out[0][i]):
            maxm = Out[0][i]
            k = i
    if (k == 0):
        print("Image is of letter A.", '\n')
    elif (k == 1):
        print("Image is of letter B.", '\n')
    else:
        print("Image is of letter C.", '\n')
    plt.imshow(x.reshape(5, 5))
    plt.show()

    return


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
    w2 = generate_wt(5, 3)
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

    # ------- ідентифікація літералів / передбачення ---------------------
    print('Вхідні параметри відповідають літералу "А"')
    print('Результат ідентифікації:')
    predict(x[0], w1, w2)

    print('Вхідні параметри відповідають літералу "В"')
    print('Результат ідентифікації:')
    predict(x[1], w1, w2)

    print('Вхідні параметри відповідають літералу "С"')
    print('Результат ідентифікації:')
    predict(x[2], w1, w2)
