def calculateZ(U, A, B):
    X = [] # not A
    A = list(A)
    U = list(U)
    Y = list(B)
    result = []
    for i in U:
        if i not in A:
            X.append(i)
    # Z = x U y = notA U B
    for i in X:
        result.append(i)
    for i in Y:
        result.append(i)
    return set(sorted(result))