from itertools import combinations

def gerar_combinacoes_e_salvar(numeros_fixos, numeros_removidos, nome_arquivo):
    conjunto_total = set(range(1, 26))
    numeros_fixos = set(numeros_fixos)
    numeros_removidos = set(numeros_removidos)

    # Calcular conjunto resultante após remoção
    conjunto_disponivel = conjunto_total - numeros_removidos

    # Garantir que os números fixos estão no conjunto disponível
    conjunto_disponivel |= numeros_fixos

    # Gerar combinações de 15 números
    combinacoes = combinations(conjunto_disponivel, 15)

    # Filtrar combinações que contenham os números fixos
    combinacoes_filtradas = [combo for combo in combinacoes if numeros_fixos.issubset(combo)]

    # Ordenar as combinações
    combinacoes_filtradas = sorted(combinacoes_filtradas)

    # Salvar os resultados no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        for combo in combinacoes_filtradas:
            arquivo.write(', '.join(map(str, combo)) + '\n')

# Exemplo de uso:
numeros_fixos = [1, 2, 3, 4, 5, 6, 12, 13, 16, 22, 23, 25]
numeros_removidos = [7, 8, 15, 17, 19]
gerar_combinacoes_e_salvar(numeros_fixos, numeros_removidos, 'resultados.txt')
