"""
Escreva um programa que peça ao usuário para digitar uma frase e, em seguida, 
imprima quantas letras essa frase possui.
"""

# Solução proposta:

letras = lambda x: len(x)

frase = input('Digite uma frase')
qtd_letras = letras(frase)
print('Quantidade de letra da frase digitada é: {}'.format(qtd_letras))
