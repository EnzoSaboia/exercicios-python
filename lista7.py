#1

dados = {"nome": "Enzo", "idade": 22, "cidade": "Curitiba"}
print(dados["nome"])
print(dados["idade"])
print(dados["cidade"])
print(dados)

#2

produtos = {"arroz": 20, "miojo": 10, "bala": 5}

produto = input("Qual produto deseja alterar? ")
novo_valor = float(input("Digite o novo valor: "))

if produto in produtos:
    produtos[produto] = novo_valor
else:
    print("Produto não encontrado")

print(produtos)

#3

dados = {}

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

dados[nome] = idade

print(dados)

#4

pares = []

for i in range(3):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    pares.append((chave, valor))

dicionario = dict(pares)

print(dicionario)

#5

dados = {"a": 1, "b": 2, "c": 3}

resp = input("Deseja apagar tudo? sim ou nao: ")

if resp.lower() == "sim":
    dados.clear()

print(dados)

#6

dic = {"nome": "Enzo", "idade": 22}

copia = dic.copy()

copia["idade"] = 30

print("Dados:", dic)
print("Cópia:", copia)

#7

nomes = input("Digite nomes separados por vírgula: ").split(",")

dicionario = dict.fromkeys(nomes, 0)

print(dicionario)

#8

alunos = {"aluno1": 8, "aluno2": 7, "aluno3": 9}

nome = input("Digite qual aluno gostaria de saber a nota: ")

nota = alunos.get(nome, "Aluno não encontrado")
print(nota)

#9

produtos = {"arroz": 20, "miojo": 10, "bala": 5}

print("Chaves:", produtos.keys())
print("Valores:", produtos.values())
print("Pares:", produtos.items())

#10

dic = {"Enzo": 22, "Pedro": 20, "Lucas": 18}

chave = input("Digite a chave que deseja excluir: ")

excluido = dic.pop(chave, "Chave não encontrada")
print("Excluído:", excluido)

dic.popitem()

nova_chave = input("Nova chave: ")
novo_valor = input("Novo valor: ")

dic.update({nova_chave: novo_valor})

print("Dicionário final:", dic)

#11

usuarios = {
    "Enzo": 22,
    "Pedro": 20,
    "Lucas": 18
}

while True:
    print("\nMenu: ")
    print("1 - Exibir usuários")
    print("2 - Buscar usuário (get)")
    print("3 - Adicionar usuário")
    print("4 - Atualizar idade")
    print("5 - Remover usuário (pop)")
    print("6 - Remover último (popitem)")
    print("7 - Copiar e alterar (copy)")
    print("8 - Criar com fromkeys")
    print("9 - Atualizar com update")
    print("10 - Limpar tudo (clear)")
    print("11 - Criar com dict()")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Nomes:", usuarios.keys())
        print("Idades:", usuarios.values())
        print("Dados completos:", usuarios.items())

    elif opcao == "2":
        nome = input("Digite o nome: ")
        idade = usuarios.get(nome, "Usuário não encontrado")
        print("Resultado:", idade)

    elif opcao == "3":
        nome = input("Novo nome: ")
        idade = int(input("Idade: "))
        usuarios[nome] = idade
        print("Usuário adicionado!")

    elif opcao == "4":
        nome = input("Nome do usuário: ")
        if nome in usuarios:
            nova_idade = int(input("Nova idade: "))
            usuarios[nome] = nova_idade
            print("Idade atualizada!")
        else:
            print("Usuário não encontrado")

    elif opcao == "5":
        nome = input("Nome para remover: ")
        removido = usuarios.pop(nome, "Usuário não encontrado")
        print("Removido:", removido)

    elif opcao == "6":
        if usuarios:
            removido = usuarios.popitem()
            print("Removido (último):", removido)
        else:
            print("Dicionário vazio")

    elif opcao == "7":
        copia = usuarios.copy()
        nome = input("Nome para alterar na cópia: ")

        if nome in copia:
            nova_idade = int(input("Nova idade: "))
            copia[nome] = nova_idade
        else:
            print("Usuário não existe na cópia")

        print("Original:", usuarios)
        print("Cópia:", copia)

    elif opcao == "8":
        nomes = input("Digite nomes separados por vírgula: ").split(",")
        idade_padrao = int(input("Idade padrão: "))

        novo_dic = dict.fromkeys([n.strip() for n in nomes], idade_padrao)
        print("Novo dicionário:", novo_dic)

    elif opcao == "9":
        novo_dic = {}
        qtd = int(input("Quantos usuários deseja adicionar? "))

        for _ in range(qtd):
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            novo_dic[nome] = idade

        usuarios.update(novo_dic)
        print("Atualizado:", usuarios)

    elif opcao == "10":
        conf = input("Tem certeza que deseja apagar tudo? (sim/nao): ")
        if conf.lower() == "sim":
            usuarios.clear()
            print("Dicionário limpo!")
        else:
            print("Operação cancelada")

    elif opcao == "11":
        lista = []
        qtd = int(input("Quantos pares deseja inserir? "))

        for _ in range(qtd):
            chave = input("Chave: ")
            valor = input("Valor: ")
            lista.append((chave, valor))

        novo_dic = dict(lista)
        print("Novo dicionário:", novo_dic)

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
