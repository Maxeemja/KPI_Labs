from random import *
m, n = randint(1,5),randint(1,5)
A = [[randrange(0,5) for y in range(n)] for x in range(m)]
for j in range(m):
    print(A[j])
k = 0
for j in range(n):
    k = 0
    for i in range(m):
        if A[i][j] % 2 == 1:
            k += 1
    print("Кількість непарних чисел у " + str(j+1) + "-ому стовпці дорівнює: " + str(k))
