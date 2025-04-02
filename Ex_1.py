# Crie uma função que receba duas listas de números inteiros e retorne uma 
# nova lista contendo os elementos que aparecem em ambas as listas (interseção).

conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

def receba(conjunto_a, conjunto_b):
    interseccao = conjunto_a & conjunto_b
    return interseccao
print(receba(conjunto_a, conjunto_b))

