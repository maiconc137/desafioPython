"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima os números pares de 0 até esse número.
"""

# Solução proposta:

def num_par(x):
    par = []
    for i in range(x):
        if i % 2 == 0:
            par.append(i)
        else:
            continue
    return par

numeros = int(input('Digite um número inteiro positivo: '))
numeros_pares = num_par(numeros)
print(numeros_pares)