"""
Crie uma função que encontre a k-ésima maior elemento em uma lista de números.
"""

# Solução proposta:

def k_esimo_maior_numero(lista: list[float], k: int) -> float:
    lista.sort(reverse=True)
    return lista[k - 1]

exemplo = [4, 2, 4.1, 5, 3, 1]
print(k_esimo_maior_numero(exemplo, 1)) # primeiro maior número
print(k_esimo_maior_numero(exemplo, 2)) # e por aí vai
print(k_esimo_maior_numero(exemplo, 3))
print(k_esimo_maior_numero(exemplo, 4))
print(k_esimo_maior_numero(exemplo, 5))
print(k_esimo_maior_numero(exemplo, 6))
