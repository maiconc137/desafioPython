"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima se esse número é par ou ímpar.
"""

# Solução proposta:

def par_impar(x):
    if (x % 2 == 0):
        return '{} é par.'.format(x)
    else:
        return '{} é ímpar.'.format(x)
res = par_impar(int(input('Digite um número: ')))
print(res)
