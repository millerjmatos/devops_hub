import random

def soma_volante(nums):
    soma = sum(nums)
    return 171 <= soma <= 220

def gerar_sorteio():
    while True:
        numeros_disponiveis = [num for num in range(1, 26)]
        
        impares = [num for num in numeros_disponiveis if num % 2 != 0]
        pares = [num for num in numeros_disponiveis if num % 2 == 0]

        num_imp = random.sample(impares, 8)
        num_par = random.sample(pares, 7)

        # Junte todos os números escolhidos, ordene-os
        numeros_sorteados = sorted(num_imp + num_par)
        if soma_volante(numeros_sorteados):
            break

    return numeros_sorteados

# Exemplo de uso
resultado_sorteio = gerar_sorteio()
print("Números Sorteados:", resultado_sorteio)

# Adicionar os números sorteados ao arquivo sem excluir o conteúdo existente
with open('resultados.txt', 'a') as arquivo:
    for i, numero in enumerate(resultado_sorteio, start=1):
        arquivo.write(str(numero))
        if i % 15 == 0:
            arquivo.write('\n')
        else:
            arquivo.write(' ')
