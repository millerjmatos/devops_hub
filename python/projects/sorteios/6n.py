import random

def tem_consecutivos(nums):
    return any(nums[i] + 1 == nums[i + 1] for i in range(len(nums) - 1))

def soma_volante(nums):
    soma = sum(nums)
    return 104 <= soma <= 226

def gerar_sorteio():
    while True:
        numeros_disponiveis = [num for num in range(1, 61) if num not in [2, 9, 18, 19, 26, 28, 44, 45, 48, 50] and num not in [4, 7, 16, 35, 46, 54]]
        
        impares = [num for num in numeros_disponiveis if num % 2 != 0]
        pares = [num for num in numeros_disponiveis if num % 2 == 0]

        num_imp = random.sample(impares, 3)
        num_par = random.sample(pares, 3)

        # Junte todos os números escolhidos, ordene-os e verifique se há consecutivos
        numeros_sorteados = sorted(num_imp + num_par)
        if not tem_consecutivos(numeros_sorteados) and soma_volante(numeros_sorteados):
            break

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
