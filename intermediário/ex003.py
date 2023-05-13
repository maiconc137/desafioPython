"""
Crie uma função que receba uma lista de números e retorne o segundo maior número da 
lista.
"""

# Solução proposta:

def segundo_maior_numero(lista: list) -> float:
    lista.sort(reverse=True)
    return lista[1]

exemplo = [
        1,
        2,
        3,
        3.1,
        3.14159,
        -100,
        0
    ]

print("O segundo maior número da lista é")
print(segundo_maior_numero(exemplo))
