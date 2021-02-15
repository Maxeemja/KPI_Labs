def fullSolution(U, A, B, C):
    U = list(U)
    A = list(A)
    B = list(B)
    C = list(C)
    notA = []
    result = []
    for i in U:
        if i not in A:
            notA.append(i)
    # проміжні множини : M , N , K , Z
    # M= a U b ; N = a U c; K = notA U c; Z = M ⋂ N ;
    M = []
    N = []
    K = []
    Z = []
    for i in A:
        M.append(i)
        N.append(i)
    for i in B:
        M.append(i)
    for i in C:
        N.append(i)
        K.append(i)
    for i in notA:
        K.append(i)
    for i in M:
        if i in N:
            Z.append(i)
    for i in Z:
        if i in K:
            result.append(i)
    result.sort()
    return set(result)
