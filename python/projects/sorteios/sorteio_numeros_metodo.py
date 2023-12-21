# Este código escolhe aleatoriamente um par e um ímpar dos números fixos e completa com mais um par e um ímpar entre 1 e 60, excluindo alguns números específicos. Ele garante que não haja repetição e ordena os resultados.

# números fixos são os 16 números mais sorteados no ano, sendo 8 pares e 8 ímpares.

# números específicos são 8 números que estão a muito tempo de fora do sorteio.

import random

def sortear_numeros():
    # Números fixos (um par e um ímpar devem ser escolhidos)
    numeros_fixos = [5, 10, 11, 13, 14, 22, 25, 32, 34, 35, 39, 43, 46, 56, 59]
    numero_fixo_par = random.choice([num for num in numeros_fixos if num % 2 == 0])
    numero_fixo_impar = random.choice([num for num in numeros_fixos if num % 2 != 0])

    # Números restantes de 1 a 60 excluindo alguns específicos (2 pares e 2 ímpares)
    numeros_excluidos = {2, 9, 19, 23, 28, 44, 45, 50}
    numeros_aleatorios = set()

    while len(numeros_aleatorios) < 4:
        if len(numeros_aleatorios) < 2:
            numero = random.randrange(1, 61, 2)  # Sortear apenas números ímpares
            if numero not in numeros_excluidos and numero != numero_fixo_impar:
                numeros_aleatorios.add(numero)
        else:
            numero = random.randrange(2, 61, 2)  # Sortear apenas números pares
            if numero not in numeros_excluidos and numero != numero_fixo_par:
                numeros_aleatorios.add(numero)

    # Juntar, ordenar e retornar os números
    numeros_sorteados = sorted(list(numeros_aleatorios | {numero_fixo_par, numero_fixo_impar}))

    return numeros_sorteados

# Exemplo de uso
numeros_sorteados = sortear_numeros()
print("Números sorteados:", numeros_sorteados)

# Adicionar os números sorteados ao arquivo sem excluir o conteúdo existente
with open('resultados.txt', 'a') as arquivo:
    for i, numero in enumerate(numeros_sorteados, start=1):
        arquivo.write(str(numero))
        if i % 6 == 0:
            arquivo.write('\n')
        else:
            arquivo.write(' ')