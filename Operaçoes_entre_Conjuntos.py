# OPERAÇÃO ENTRE CONJUNTOS

# Definir dois Conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# União : todos os elementos de ambos 
uniao = conjunto_a | conjunto_b
print(uniao)

# Intersecção : elementos comuns aos conjuntos
interseccao = conjunto_a & conjunto_b
print(interseccao)

# Diferença : elementos que estão no conjunto A, mas não estão no conjunto B

diferenca = conjunto_a - conjunto_b
print(diferenca)

# Diferença simétrica : elementos que estão em um outro conjunto, mas não estão em ambos
diferenca_simetrica = conjunto_a ^ conjunto_b
print(diferenca_simetrica)