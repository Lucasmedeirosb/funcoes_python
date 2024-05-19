#def funcao():
#    print("Bloco de código")
def imprime_nome(nome):
    print(f"Nome: {nome}")

def piramide(numero):
    for contador in range(1, numero+1):
        for contador1 in range(0, contador, 1):
            print(contador, end=" ")
        print()

def piramide2 (numero):
    for contador in range(1, numero+1):
        for contador1 in range(1, contador, 1):
            print(contador1, end=" ")
        print()

def exercicio4(texto):
    cont = 0
    for contador in texto:
        if contador in "aeiouAEIOU":
            cont = cont + 1
    print(f"O texto {texto} possui {cont} vogais!")

def exercicio5(produto, quantidade, valor_unidade):
    mult = quantidade * valor_unidade
    return f"Você tem o total de R${mult} em estoque, de {produto}"

def exercicio6(n1, n2):
    soma = n1 + n2
    return f"Você tem o total de R${soma}"

def exercicio7(*num):
    soma = 0
    for contador in range(len(num)):
        soma = soma + num[contador]
    return soma

def exercicio8(texto1):
    tamanho = len(texto1)
    cont = 0
    for contador in range(tamanho-1, -1, -1):
        print(texto1[contador], end="")
        if texto1[contador] != " " and texto1[contador] != "." and texto1[contador] != ",":
            cont = cont + 1
    print()
    print(cont)
    
def exercicio9(n):#slice para inverter
    print(n[::-1])

def exercicio10(lista):
    nova_lista = []
    for contador in lista:
        if contador not in nova_lista:#se contador não estiver em nova_lista
            nova_lista.append(contador)
    print(nova_lista)
    
def exercicio11(lista):
    nova_lista = sorted(set(lista))  # Remove duplicatas e ordena a lista
    print(nova_lista)

def exercicio12(numero):
    if numero != 1:
        for contador in range(2, numero-1, 1):
            if numero%contador==0:
                return f"Esse número não é primo"
    return f"Esse npumero é primo"
