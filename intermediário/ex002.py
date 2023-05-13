"""
Crie uma função que receba uma lista de strings e retorne a string mais longa da lista.
"""

# Solução proposta:

def string_mais_longa(lista: list) -> str:
    maior_comprimento = -1
    for i in range(len(lista)):
        comprimento_string = len(lista[i])
        if comprimento_string > maior_comprimento:
            maior_comprimento = comprimento_string
            maior_string = i

    return lista[maior_string]

# Solução alternativa utilizando o método sort
# def string_mais_longa(lista: list) -> str:
#     lista.sort(reverse=True, key=lambda x: len(x))
#     return lista[0]

exemplo = [
        "teste",
        "teste1",
        "teste2",
        "teste_versão_final",
        "teste_final_final"
    ]

print("A string mais longa da lista é")
print(string_mais_longa(exemplo))
