import random

# 2 (dois) conjuntos vazios para armazenar números pares e ímpares:
numeros_pares = set()
numeros_impares = set()

# Loop para gerar 8 números pares aleatórios sem repetição:
while len(numeros_pares) < 8:
    numero = random.randint(1, 25)
    if numero % 2 == 0 and numero not in numeros_pares:
        numeros_pares.add(numero)

# Loop para gerar 8 números ímpares aleatórios sem repetição:
while len(numeros_impares) < 8:
    numero = random.randint(1, 25)
    if numero % 2 == 1 and numero not in numeros_impares:
        numeros_impares.add(numero)

# Convertemos os conjuntos em listas para que possamos combiná-las:
numeros_pares = list(numeros_pares)
numeros_impares = list(numeros_impares)

# Combina as duas listas para obter a lista final com 16 números mistos:
numeros_sorteados = numeros_pares + numeros_impares

# Ordena a lista final em ordem crescente:
numeros_sorteados.sort()

# Imprime a lista final de 16 números em ordem crescente:
print(numeros_sorteados)

# Abre o arquivo 'sorteados.txt' no modo 'append' e escreve o resultado nele:
with open('sorteados.txt', 'a') as arquivo:
    # Converte os números em strings para escrevê-los no arquivo.
    numeros_formatados = [str(numero) for numero in numeros_sorteados]
    # Escreve os números no arquivo, separados por vírgulas e seguidos de uma quebra de linha:
    arquivo.write(', '.join(numeros_formatados) + '\n')
