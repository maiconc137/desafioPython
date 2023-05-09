"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima o fatorial desse número.
"""

# Solução proposta:

def fatorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    fat = 1
    for i in range(2, num + 1):
      fat *= i
    return fat

numero = int(input("Digite um número: "))
resultado = fatorial(numero)
print("O fatorial de", numero, "é", resultado)
