from itertools import combinations

# Conjuntos 
A = [3, 14, 18, 47, 59]
B = [10, 12, 25, 32, 48]

# Gera todas as combinações possíveis
combinacoes = []

for elemento_b in B:
    # Combinando os elementos de A com um elemento de B
    combinacoes.extend(combinations(sorted(A + [elemento_b]), 6))

for elemento_a in A:
    # Combinando os elementos de B com um elemento de A
    combinacoes.extend(combinations(sorted(B + [elemento_a]), 6))

# Imprime as combinações separadas por linha
for combinacao in combinacoes:
    print(combinacao)

