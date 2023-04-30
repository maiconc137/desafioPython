"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima os números de 0 até esse número, mas substitua os múltiplos de 3 por "Fizz" e 
os múltiplos de 5 por "Buzz".
"""

# Solução proposta:

def fizz_buzz(x):
    lista = []
    for i in range(1, x):
        if i % 3 == 0:
            lista.append('Fizz')
        elif i % 5 == 0:
            lista.append('Buzz')
        else:
            lista.append(i)
    return lista

num = int(input('Digite um número: '))
nova_lista = fizz_buzz(num)