"""
Crie uma função que receba uma lista de números e retorne a média aritmética dos 
números pares.
"""

# Solução proposta:

# lista proposta
lista = [1,2,3,4,5,6,7,8,9]
# lista que recebera os valores pares
lista_par = []

# função que verifica qual número da lista é par
def num_par(lista_num):
    for i in lista_num:
        if (i % 2 == 0):
            lista_par.append(i)
    return lista_par

# função que calcula a média dos números pares
def media_par(x):
    tam = len(x)
    soma = 0
    for i in x:
        soma += i
    return soma / tam

# guardando o resultado em uma variável e imprimindo na tela o resultado
resultado = media_par(num_par(lista))
print(resultado)
