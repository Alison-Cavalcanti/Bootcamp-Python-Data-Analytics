# Entrada dos valores da capacidade atual e do aumento percentual
# Utilizamos a função input() para receber a entrada do usuário, que será uma string contendo os valores separados por espaço
# Em seguida, utilizamos a função split() para dividir essa string nos espaços e obter uma lista de strings contendo os valores individuais
# Em seguida, usamos a função map() para aplicar a função int() a cada elemento da lista de strings
# Isso transformará cada string em um número inteiro
# Finalmente, usamos a função tuple() para converter o resultado em uma tupla contendo os valores inteiros
capacidade_atual, aumento_percentual = map(int, input().split())

# Calcula a nova capacidade total após o aumento percentual
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)

# Imprime a nova capacidade total, arredondando para o número inteiro mais próximo
print(int(nova_capacidade))
