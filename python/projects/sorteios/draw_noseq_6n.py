import random

def gerar_sorteio():
    # Passo 1: Escolha aleatoriamente um número par e um número ímpar do conjunto fixo
    numeros_fixos = [5, 10, 11, 13, 14, 22, 25, 32, 34, 35, 39, 43, 46, 56, 59]
    pares_fixos = [num for num in numeros_fixos if num % 2 == 0]
    impares_fixos = [num for num in numeros_fixos if num % 2 != 0]

    numero_par_escolhido = random.choice(pares_fixos)
    numero_impar_escolhido = random.choice(impares_fixos)

    # Passo 2: Escolha aleatoriamente dois números ímpares e dois números pares
    numeros_disponiveis = [num for num in range(1, 61) if num not in [2, 9, 19, 23, 28, 44, 45, 50] and num not in numeros_fixos]
    
    impares = [num for num in numeros_disponiveis if num % 2 != 0]
    pares = [num for num in numeros_disponiveis if num % 2 == 0]

    dois_impares = random.sample(impares, 2)
    dois_pares = random.sample(pares, 2)

    # Garante que os números não sejam iguais aos escolhidos no Passo 1
    while numero_par_escolhido in dois_impares or numero_par_escolhido in dois_pares or numero_impar_escolhido in dois_impares or numero_impar_escolhido in dois_pares:
        dois_impares = random.sample(impares, 2)
        dois_pares = random.sample(pares, 2)

    # Garante que não haja números consecutivos
    for nums in [dois_impares, dois_pares]:
        nums.sort()
        while nums[0] + 1 == nums[1]:
            random.shuffle(nums)

    # Junte todos os números escolhidos, ordene-os e retorne a lista
    numeros_sorteados = [numero_par_escolhido, numero_impar_escolhido] + dois_impares + dois_pares
    numeros_sorteados.sort()

    return numeros_sorteados

# Exemplo de uso
resultado_sorteio = gerar_sorteio()
print("Números Sorteados:", resultado_sorteio)

# Adicionar os números sorteados ao arquivo sem excluir o conteúdo existente
with open('resultados.txt', 'a') as arquivo:
    for i, numero in enumerate(resultado_sorteio, start=1):
        arquivo.write(str(numero))
        if i % 6 == 0:
            arquivo.write('\n')
        else:
            arquivo.write(' ')