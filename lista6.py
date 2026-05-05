#1

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor

print("Soma total:", soma)

#2

n = int(input("Digite n: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for linha in matriz:
    print(linha)

#3

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

num = int(input("Digite um número: "))
encontrado = False

for linha in matriz:
    if num in linha:
        encontrado = True

print("Está na matriz!" if encontrado else "Não está.")

#4

matriz = [
    [1, 2],
    [3, 4]
]

matriz[0], matriz[1] = matriz[1], matriz[0]

for linha in matriz:
    print(linha)

#5

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k = float(input("Digite o escalar: "))

for i in range(3):
    for j in range(3):
        matriz[i][j] *= k

for linha in matriz:
    print(linha)

#6

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            pares += 1

print("Quantidade de pares:", pares)

#7

import random

matriz = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

maior = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

for linha in matriz:
    print(linha)

print("Maior:", maior)

#8

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    media = sum(linha) / len(linha)
    print("Média:", media)

#9

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma = 0
for i in range(4):
    soma += matriz[i][i]

print("Soma da diagonal:", soma)

#10

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

transposta = []

for j in range(len(matriz[0])):
    linha = []
    for i in range(len(matriz)):
        linha.append(matriz[i][j])
    transposta.append(linha)

for linha in transposta:
    print(linha)

#11

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

somas = [0, 0, 0]

for i in range(3):
    for j in range(3):
        somas[j] += matriz[i][j]

print(somas)

#12

matriz = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

simetrica = True

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False

print("Simétrica" if simetrica else "Não é")

#13

matriz = [[i + j for j in range(5)] for i in range(5)]

for i in range(5):
    print(matriz[i][4 - i])

#14

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            resultado[i][j] += A[i][k] * B[k][j]

for linha in resultado:
    print(linha)

#15

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matriz)

rotacionada = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotacionada[j][n - 1 - i] = matriz[i][j]

for linha in rotacionada:
    print(linha)
