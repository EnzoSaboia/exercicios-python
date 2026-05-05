#1

a = []

for i in range(10):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            a.append(num)
            break
        except ValueError:

            print("Entrada inválida. Por favor, digite um número inteiro.")

print("\nLista 'a' completa:", a)

#2

numeros = [1,2,3,4,5,6]

for i in range(6):
    print(numeros[i])

#3

numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

menor = min(numeros)
maior = max(numeros)

print(menor)
print(maior)

#4

notas_alunos = []
abaixo_media = 0
acima_media = 0

cont = int(input("Quantos alunos têm na sala? "))

for i in range(cont):
    nota = int(input(f"Qual a nota do aluno {i + 1}? "))
    notas_alunos.append(nota)

    if nota < 60:
        abaixo_media += 1
    else:
        acima_media += 1

print(f"\nAlunos abaixo da média: {abaixo_media}")
print(f"Alunos na média ou acima: {acima_media}")

#5

numeros = []
pares = []
impares = []

for i in range(1, 6):
    num = int(input(f"Digite o {i}º número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

soma = sum(numeros)
media = soma / len(numeros)

print("-" * 20)
if pares:
    print(f"Maior número par: {max(pares)}")
else:
    print("Não foram digitados números pares.")

if impares:
    print(f"Menor número ímpar: {min(impares)}")
else:
    print("Não foram digitados números ímpares.")

print(f"Somatório de todos os elementos: {soma}")
print(f"Média dos valores: {media:.2f}")
