import numpy as np


def randSet(amount):
    randNums = np.random.randint(0, 255, amount)
    return set(randNums)


def setCreating(string):
    result = []
    string = string.replace('{', '').replace('}', '').replace(' ', '').split(',')
    for el in string:
        try:
            if (not 0 <= int(el) <= 255):
                return False
            result.append(int(el))
        except ValueError:
            continue

    return set(result)


def createUniversal(string):
    string = string.replace('{', '').replace('}', '').replace(' ', '').split(',')
    result = []
    for j in range(int(string[0]), int(string[1]) + 1):
        result.append(j)

    return set(result)


# unification U
def unification(x, y):
    x = list(x)
    y = list(y)
    z = []
    for i in x:
        z.append(i)
    for i in y:
        if i not in z:
            z.append(i)

    return set(sorted(z))


# ∩
def intersection(x, y):
    x = list(x)
    y = list(y)
    z = []
    for j in range(len(x)):
        for i in range(len(y)):
            if x[j] == y[i]:
                z.append(x[j])
    z.sort()
    return set(z)


# ¬
def nope(u, y):
    u = list(u)
    y = list(y)
    result = []
    for i in u:
        if i not in y:
            result.append(i)
    result.sort()
    return set(result)




