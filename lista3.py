#1
lista = [5, 2, 8, 1, 9]

maior_valor = max(lista)
print(maior_valor)


lista = [15, 4, 3, 7, 9]

menor_valor = min(lista)
print(menor_valor)

#2
x = int(input("Qual o número de alunos na turma? "))

lista = []

for i in range(x):
    nome = input(f"Digite seu nome: {i + 1}: ")
    lista.append(nome)

for nome in lista:
    print(nome)

#3

Lista = [10, 50, 5, 2, 100]
i=0
while i < 5:
    print(Lista[i])
    i=i+1

#4

lista_A = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista_A.append(numero)

    print(f"Os números inseridos são: {lista_A}")
