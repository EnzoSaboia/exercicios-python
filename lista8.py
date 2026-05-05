#1

lista = [1, 2, 3, 4, 5]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

#2

lista = ['vermelho', 'azul', 'verde', 'amarelo']
print(lista[1])

#3

lista = [1, 2, 3]
lista.append(10)
print(lista)

#4

frutas = ['maçã', 'banana', 'laranja']
frutas.remove('banana')
print(frutas)

#5

lista = [10, 20, 30, 40, 50]
tamanho = len(lista)
print("O tamanho dessa lista é: %d " % tamanho)

#6

lista = [1, 3, 5, 7, 9]
print(7 in lista)

#7

lista1 = [1,2]
lista2 = [3,4]
lista3 = []

lista3.append(lista1)
lista3.append(lista2)

i=0
while i<len(lista3):
    print(lista3[i])
    i=i+1

#8

lista = ['a','b','c','d']
nova_lista = lista[::-1]
print(nova_lista)

#9

lista_numeros = [1, 2, 2, 3, 2, 4]

quantidade = lista_numeros.count(2)

print(f"O número 2 aparece {quantidade} vezes")

#10

lista_precos = [10.5, 20.0, 15.5]
soma = sum(lista_precos)
print(f"A soma de todos os elementos é: {soma:.2f}")

#11

def remover_duplicatas(lista):
    return list(dict.fromkeys(lista))

lista = [1, 1, 2, 3, 3, 4, 5, 5, 5]

resultado = remover_duplicatas(lista)

print(resultado)

#12

lista = [3, 8, 1, 5, 2]

maior = lista[0]
menor = lista[0]

for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Maior: ", maior)
print("Menor: ", menor)

#13

quadrados = [x**2 for x in range (1,11)]
print(quadrados)

#14

lista = [1, 2, 3, 4, 5, 6, 7]
impares = [x for x in lista if x % 2 != 0]
print(impares)

#15

def rotacionar(lista, n):
    n = n % len(lista)
    return lista[-n:] + lista[:-n]

lista = [1, 2, 3, 4, 5]
print(rotacionar(lista, 2))

#16

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

intersecao = []

for x in lista1:
    if x in lista2 and x not in intersecao:
        intersecao.append(x)

print(intersecao)

#17

matriz = [[1, 2],
          [3,4],
          [5,6]]

flatten = [item for sublista in matriz for item in sublista]
print(flatten)

#18

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)


def merge(esq, dir):
    resultado = []
    i = 0
    j = 0

    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    while i < len(esq):
        resultado.append(esq[i])
        i += 1

    while j < len(dir):
        resultado.append(dir[j])
        j += 1

    return resultado

lista = [5, 2, 9, 1, 3]
ordenada = merge_sort(lista)

print("Original:", lista)
print("Ordenada:", ordenada)

#19

def kadane(lista):
    max_atual = max_global = lista[0]

    for num in lista[1:]:
        max_atual = max(num, max_atual + num)
        if max_atual > max_global:
            max_global = max_atual

    return max_global

lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = kadane(lista)
print(resultado)

#20

def permutacoes(lista):
    if len(lista) == 1:
        return [lista]

    resultado = []

    for i in range(len(lista)):
        atual = lista[i]
        resto = lista[:i] + lista[i+1:]

        for p in permutacoes(resto):
            resultado.append([atual] + p)

    return resultado

lista = [1, 2, 3]
print(permutacoes(lista))
