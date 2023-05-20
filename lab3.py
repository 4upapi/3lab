#30.	Формируется матрица F следующим образом: если в В количество простых чисел в нечетных столбцах в области 2 больше,
# чем произведение чисел по периметру области 3,
# то поменять в В симметрично области 1 и 3 местами,
# иначе С и В поменять местами несимметрично.
# При этом матрица А не меняется.
# После чего вычисляется выражение: ((К*A T)*(F+А)-K* F T .
# Выводятся по мере формирования А, F и все матричные операции последовательно.

from random import randint
print('Введите N:', end=' ')
n = int(int(input()))
print('Введите K:', end=' ')
k = int(int(input()))
a = []
F = []
Atrans = []
FA = []
Ftrans = []
Raz = []
Proizv = []
kol = 0
chisl = 1
nado = 0
colich =0
a = [2,3,5,7]
for i in range(n):
    F.append([0]*n)
    Atrans.append([0]*n)
    FA.append([0]*n)
    Ftrans.append([0] * n)
    Raz.append([0] * n)
    Proizv.append([0] * n)
print('Основная матрица')
for i in range(len(F)):
    for j in range(len(F)):
        F[i][j] = randint(-10,10)
        print("{:4d}".format(F[i][j]), end = "")
    print()
print()
A = F
if (n // 2) % 2 != 0:
    for i in range(0,n//4+1):
        for j in range(0, n //  4+1):
            if j %2 ==0 and i <= j :
                if F[i][j] in a:
                    kol += 1
    for i in range(0, n//4+1):
        for j in range(n//4+1, n // 2):
            if j %2 ==0 and i <= n//2 -(j+1):
                if F[i][j] in a:
                    kol +=1
    for i in range(0,n//4+1):
        for j in range(n // 4 , n//2):
            if i == n//2 -(j+1):
                chisl *= F[i][j]
    for i in range(n//4+1,n//2):
        for j in range(n // 4 , n//2):
            if i == j:
                chisl *= F[i][j]
    for i in range(1, n//2-1):
        chisl += 1
elif (n // 2)%2==0:
    for i in range(0, n // 4):
        for j in range(0, n // 4 + 1):
            if j %2 == 0 and i <= j:
                if F[i][j] in a:
                    kol += 1
    for i in range(0, n // 4 + 1):
        for j in range(n // 4 + 1, n // 2):
            if j %2 == 0 and i <= n // 2 - (j + 1):
                if F[i][j] in a:
                    kol += 1
    for i in range(0, n // 4 + 1):
        for j in range(n // 4, n // 2):
            if i == n // 2 - (j + 1):
                chisl *= F[i][j]
    for i in range(n // 4 , n // 2):
        for j in range(n // 4, n // 2):
            if i == j:
                chisl *= F[i][j]
    for i in range(1, n // 2 - 1):
        chisl += 1
if kol > chisl:
    print("Изменённая матрица")
    for i in range(0, n // 4):
        for j in range(n // 4, n // 2+2):
            if i >= n // 2 - (j+1):
                F[i][j], F[i][n//2-j-1] = F[i][n//2-j-1], F[i][j]
    for i in range(n // 4+1, n // 2):
        for j in range(n // 4, n // 2):
            if i <= j:
                F[i][j], F[i][n // 2 - j - 1] = F[i][n // 2 - j - 1], F[i][j]
    for i in range(len(F)):
        for j in range(len(F)):
            print("{:4d}".format(F[i][j]), end="")
        print()
    print()
elif kol <= chisl:
    print("Изменённая матрица")
    for i in range(0, n//2):
        for j in range(0,n//2):
            F[i][j], F[i][j + n//2] = F[i][j + n//2], F[i][j]
    for i in range(len(F)):
        for j in range(len(F)):
            print("{:4d}".format(F[i][j]), end="")
        print()
    print()
print("K * A транспонированная")
for i in range(len(F)):
    for j in range(len(F)):
        Atrans[i][j] = k * A[j][i]
        print("{:4d}".format(Atrans[i][j]), end="")
    print()
print("F+А")
for i in range(len(F)):
    for j in range(len(F)):
        FA[i][j] = F[i][j] + A[i][j]
        print("{:4d}".format(Atrans[i][j]), end="")
    print()
print("(К*A T)*(F+А)")
for ch1 in range(n):
    for ch2 in range(n):
        for ch3 in range(n):
            nado = nado + (Atrans[ch1][ch3] * FA[ch3][ch2])
        Proizv[ch1][ch2] = nado
        nado = 0
print("K * F транспонированная")
for i in range(len(F)):
    for j in range(len(F)):
        Ftrans[i][j] = k * F[j][i]
        print("{:4d}".format(Atrans[i][j]), end="")
    print()
print("((К*A транспонированная)*(F+А)-K* F транспонированная")
for i in range(len(F)):
    for j in range(len(F)):
        Raz[i][j] = Proizv[i][j] - Ftrans[i][j]
        print("{:4d}".format(Raz[i][j]), end="")
    print()
