"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima se esse número é positivo, negativo ou zero.
"""

# Solução proposta:

def sinal(x):
    if not x:
        return 'Número é zero'
    elif (x < 0):
        return 'Número negativo'
    else:
        return 'Número positivo'


num = int(input('Digite um número: '))
print(sinal(num))
