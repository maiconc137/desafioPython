"""
Escreva um programa que peça ao usuário para digitar dois números e, em seguida,
imprima o produto desses números.
"""

# Solução proposta:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
multi = lambda x,y: x * y
res = multi(num1, num2)

print('Resultado do produto destes número é: {}'.format(res))
