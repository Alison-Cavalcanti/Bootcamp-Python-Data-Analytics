# Desafio: A Aventura do Explorador

# Entrada: Solicita ao usuário a quantidade de passos que o explorador deve dar na floresta.
quantidade_passos = int(input())

# Verificação se a quantidade de passos é positiva
if quantidade_passos == 0:
    # Se a quantidade de passos for zero, imprime a mensagem "Nenhum passo dado na floresta."
    print("Nenhum passo dado na floresta.")
else:
    # Caso contrário, utiliza um loop for para imprimir a mensagem do explorador, indicando o número do passo.
    for n in range(1, quantidade_passos + 1):
        # Verifica se o número do passo é igual a 1 (singular) ou maior que 1 (plural)
        if n == 1:
            # Se for 1, imprime a mensagem no singular: "Explorador: 1 passo"
            print(f"Explorador: {n} passo")
        else:
            # Caso contrário, imprime a mensagem no plural: "Explorador: {n} passos"
            print(f"Explorador: {n} passos")
