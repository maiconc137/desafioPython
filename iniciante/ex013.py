"""
Escreva um programa que peça ao usuário para digitar uma palavra e, em seguida, 
imprima se essa palavra é um palíndromo (ou seja, se ela pode ser lida da mesma forma 
da esquerda para a direita e da direita para a esquerda).
"""

# Solução proposta:

palavra = input('Digite uma palavra: ')
palavra_invertida = palavra[::-1]

if palavra_invertida == palavra:
    print('{} é um palíndromo'.format(palavra))
else:
    print('{} não é palíndromo'.format(palavra))
    