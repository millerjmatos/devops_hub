from itertools import combinations

# Conjuntos 
A = [3, 14, 18, 36, 47, 59]
B = [10, 12, 17, 25, 32, 48]

# Gera todas as combinações possíveis
combinacoes = []

for grp_b in B:
    # Combinando os elementos de A com um elemento de B
    combinacoes.extend(combinations(A + [grp_b], 7))

for grp_a in A:
    # Combinando os elementos de B com um elemento de A
    combinacoes.extend(combinations(B + [grp_a], 7))

# Imprime as combinações separadas por linha
for combinacao in combinacoes:
    print(combinacao)
