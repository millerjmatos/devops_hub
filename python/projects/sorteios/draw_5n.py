import random

def sortear_numeros():
    # Passo 1: Escolher aleatoriamente um número dos números fixos
    numeros_fixos = [5, 10, 11, 13, 14, 22, 25, 32, 34, 35, 39, 43, 46, 56, 59]
    numero_fixo = random.choice(numeros_fixos)

    # Passo 2: Escolher aleatoriamente dois números ímpares e dois números pares dos números restantes
    numeros_excluidos = {2, 9, 19, 23, 28, 44, 45, 50}
    numeros_aleatorios = set()

    while len(numeros_aleatorios) < 4:
        if len(numeros_aleatorios) < 2:
            numero = random.randrange(1, 61, 2)  # Sortear apenas números ímpares
            if numero not in numeros_excluidos and numero != numero_fixo:
                numeros_aleatorios.add(numero)
        else:
            numero = random.randrange(2, 61, 2)  # Sortear apenas números pares
            if numero not in numeros_excluidos and numero != numero_fixo:
                numeros_aleatorios.add(numero)

    # Passo 3: Juntar, ordenar e retornar os números
    numeros_sorteados = sorted(list(numeros_aleatorios | {numero_fixo}))

    return numeros_sorteados

# Exemplo de uso
numeros_sorteados = sortear_numeros()
print("Números sorteados:", numeros_sorteados)
