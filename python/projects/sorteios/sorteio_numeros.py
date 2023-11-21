import random

# 2 (duas) listas vazias para armazenar números pares e ímpares:
numeros_pares = []
numeros_impares = []

# Loop para gerar 8 números pares aleatórios:
for _ in range(8):
    numero = random.randint(1, 25)  # Gera um número inteiro aleatório entre 1 e 25.
    # Verifica se o número gerado é ímpar e, se for, adiciona 1 para torná-lo par.
    if numero % 2 == 1:
        numero += 1
    numeros_pares.append(numero)  # Adiciona o número par à lista de números pares.

# Loop para gerar 8 números ímpares aleatórios.
for _ in range(8):
    numero = random.randint(1, 25)  # Gera um número inteiro aleatório entre 1 e 25.
    # Verifica se o número gerado é par e, se for, adiciona 1 para torná-lo ímpar.
    if numero % 2 == 0:
        numero += 1
    numeros_impares.append(numero)  # Adiciona o número ímpar à lista de números ímpares.

# Combina as duas listas para obter a lista final com 16 números mistos.
numeros_sorteados = numeros_pares + numeros_impares

# Embaralha a lista final:
# random.shuffle(numeros_sorteados)

# Ordena a lista final em ordem crescente:
numeros_sorteados.sort()

# Imprime a lista final de 16 números em ordem crescente:
print(numeros_sorteados)

# Abre o arquivo 'sorteados.txt' no modo 'append' e escreve o resultado nele:
with open('sorteados.txt', 'a') as arquivo:
    # Converte os números em strings para escrevê-los no arquivo.
    numeros_formatados = [str(numero) for numero in numeros_sorteados]
    # Escreve os números no arquivo, separados por vírgulas e seguidos de uma quebra de linha.
    arquivo.write(','.join(numeros_formatados) + '\n')