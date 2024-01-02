import math

# Função para calcular combinações
def calcular_combinacoes(total_elementos, escolhidos):
    return math.comb(total_elementos, escolhidos)

# Parâmetros do exemplo
elementos_possiveis = 25
elementos_no_volante = 15
elementos_fixos = 13
elementos_removidos = 5

total_possibilidades = elementos_possiveis - elementos_removidos

# Calcular elementos a serem escolhidos no volante
elementos_a_escolher = elementos_no_volante - elementos_fixos

# Calcular combinações
resultado_combinacoes = calcular_combinacoes(total_possibilidades - elementos_fixos, elementos_a_escolher)

# Imprimir resultado
print(f"Total de combinações possíveis: {resultado_combinacoes}")
