#Crie uma função que recebe o nome de um produto, a quantidadde qie tem, no estoque e o valor unitário do produto.
#retorne o valor total do meu erstoque
from funcoes import exercicio5
produto = input("Digite o nome do Produto: ")
quantidade = int(input("Digite a quantidade: "))
valor_unidade = float(input("Digite o valor:"))
resposta = exercicio5(produto, quantidade, valor_unidade)#reposta recebe o retorno
print(resposta)


