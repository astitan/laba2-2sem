import numpy as np
import time
import random

K = int(input("Введите число K-ранг матрицы(не более 20): "))
while (K < 1) or (K > 20):
    K = int(input("Введите число K-ранг матрицы(не более 20): "))
T = int(input("Введите число T-количество знаков после запятой(не более 20): "))
while (T < 1) or (T > 20):
    T = int(input("Введите число T-количество знаков после запятой(не более 20): "))
X = np.zeros((K,K), dtype = int)
for i in range(K):                                                      #заполняем матрицу X
    for j in range(K):
        X[i][j] = random.randint(-2,2)
while np.linalg.matrix_rank(X) != K:
    for i in range(K):                                                  # заполняем матрицу снова X, если ранг не соответствует заданному
        for j in range(K):
            X[i][j] = random.randint(-2, 2)
current_matrix = np.zeros((K,K), dtype = int)
current_matrix = X
sum = 0
current_fakt = 1
print("m: ",current_matrix)
for n in range(1, 50):
    if n == 1:
        current_matrix = X
        current_fakt = 1
    if n > 1:
        if n == 2:
            current_fakt = current_fakt * n * 3
        else:
            current_fakt = current_fakt *70*n*n* (2*n - 2) * (2 * n - 1)
        current_matrix = np.dot(current_matrix, X)
        current_matrix = np.dot(current_matrix, X)
    sum = sum + (-1)**(n-1) * np.linalg.det(current_matrix) / current_fakt
    print("n: ",n)
    print("matrix: ",np.linalg.det(current_matrix))
    print("fakt: ",current_fakt)
    print("sum: ",sum)
    if abs(sum) <= 10**(-T):
        print("Сумма ЗЧР равна: ", sum)
        break
