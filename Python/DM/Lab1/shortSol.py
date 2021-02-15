def shortSolution(A, B, C):
    # U
    A = list(A)
    B = list(B)
    Z = []
    result = []
    for i in A:
        Z.append(i)
    for i in B:
        Z.append(i)
    for i in Z:
        if i in C:
            result.append(i)
    result.sort()
    return set(result)