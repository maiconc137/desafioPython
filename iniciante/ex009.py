"""
Escreva um programa que peça ao usuário para digitar seu nome e idade e, em seguida, 
imprima "Olá, <nome>! Você tem <idade> anos." na tela.
"""

# Solução proposta:

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

print('\nOlá {}, você tem {} anos\n'.format(nome, idade))
