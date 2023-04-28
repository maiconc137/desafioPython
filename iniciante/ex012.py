"""
Escreva um programa que peça ao usuário para digitar seu nome e, em seguida, 
imprima seu nome ao contrário (de forma diferente do exercício anterior).
"""

# Solução proposta:

def inverte_palavra(palavra):
    palavra_invertida = ''
    for letra in palavra:
        palavra_invertida = letra + palavra_invertida
    return palavra_invertida

nome = input('Digite seu nome: ')
nome_invertido = inverte_palavra(nome)
print(nome_invertido)
