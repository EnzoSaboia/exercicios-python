#1

def somar(a, b):
    return a + b

resultado = somar(2, 3)
print(resultado)

#2

def multiplicar(a, b):
    return a * b

resultado = multiplicar(2, 3)
print(resultado)

#3

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao ("Enzo")

#4

def maior(a, b):
    if a > b:
        maior = a
        return maior
    else:
        maior = b
        return maior
resultado = maior(2, 4)
print(resultado)

#5

def dividir(a, b):
    quociente = a // b
    resto = a % b
    print(f"Quociente: {quociente}, Resto: {resto}")
    return quociente, resto

#6

def par_ou_impar(n):
    resultado = n % 2 == 0
    print(resultado)
    return resultado

#7

#Será exibido:
#Olá
#None

#8

def apresentar(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

#9

def apresentar(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

apresentar('Enzo', 22, 'Curitiba')

#10

#Retornaria fora de ordem, visto que os argumentos não foram nomeados.

#11e12

def saudacao(nome, periodo='dia'):
    print(f"Bom {periodo}, {nome}!")

saudacao('Enzo')

saudacao('Enzo', 'noite')

#13

#Se você fornece um argumento opcional, o programa vai esperar que todos os proximos tbm sejam
#Entao, o correto seria:

def exemplo(a, b=1):
    print(a, b)

#14

def somar_todos(*numeros):
    resultado = sum(numeros)
    print("Soma:", resultado)
    return resultado

somar_todos(1, 2, 3, 4)

#15

def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Enzo", idade=20, cidade="Curitiba")

#16

#args são argumentos posicionais, já kwargs sao argumentos nomeados

def exemplo_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

exemplo_args_kwargs(1, 2, 3, nome="Enzo", idade=20)

#17

#Serã exibidos:
#5
#10

#18

contador = 0

def incrementar():
    global contador
    contador += 1
    print("Contador:", contador)

incrementar()
incrementar()

#19

def triplo(x):
    resultado = x * 3
    print("Triplo:", resultado)
    return resultado

f = triplo
f(5)

#20

def executar(funcao, valor):
    resultado = funcao(valor)
    print("Executar:", resultado)
    return resultado

executar(lambda x: x * 3, 4)

#21

quadrado = lambda x: x ** 2
print("Quadrado:", quadrado(5))

#22

lista = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, lista))
print("Dobro:", dobrados)

#23

lista = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, lista))
print("Pares:", pares)

#24

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print("Fatorial:", fatorial(5))

#25

def contagem(n):
    if n < 0:
        return
    print(n)
    contagem(n - 1)

contagem(5)

#26

#Essa função daria erro de recursão infinita!

#27

def media(lista):
    resultado = sum(lista) / len(lista)
    print("Média:", resultado)
    return resultado

media([10, 20, 30])

#28

def media(lista):
    resultado = sum(lista) / len(lista)
    print("Média:", resultado)
    return resultado

media([10, 20, 30])

help(media)

#29

def calculadora(a, b, operacao):
    if operacao == '+':
        resultado = a + b
    elif operacao == '-':
        resultado = a - b
    elif operacao == '*':
        resultado = a * b
    elif operacao == '/':
        resultado = a / b
    else:
        print("Operação inválida")
        return

    print("Resultado:", resultado)
    return resultado

calculadora(10, 5, '+')

#30

def processar_dados(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

processar_dados(1, 2, 3, nome="Enzo", curso="ES")
