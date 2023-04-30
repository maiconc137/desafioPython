"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima a soma de todos os números de 1 até esse número.
"""

# Solução proposta:

def soma(x):
    lista_soma = []
    y = 1
    while y <= x:
        lista_soma.append(y)
        y += 1
    return sum(lista_soma)

num = int(input('Digite um número: '))
nova_lista_soma = soma(num)
print(nova_lista_soma)
