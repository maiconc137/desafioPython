"""
Crie uma função que receba um texto como entrada e retorne uma lista com as palavras 
que aparecem mais de uma vez no texto, junto com a quantidade de vezes que cada 
palavra aparece.
"""

# Solução proposta:

def contaPalavras(texto: str) -> dict:
    texto = texto.replace(",", "") # tiramos alguns caracteres
    texto = texto.replace(".", "") # desnecessários do texto
    texto = texto.replace("\n","")

    palavras = texto.split(" ")
    contagem = {}
    for palavra in palavras:
        if palavra in contagem.keys():
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    # queremos apenas repetidas
    contagem = {k:v for k,v in contagem.items() if v > 1}
    return contagem

texto = """
Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.
"""
d = contaPalavras(texto)
for k,v in d.items():
    print(k, v)
