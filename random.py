import time

def escolha_aleatoria(lista):
    tamanho_lista = len(lista)
    tempo_atual = int(time.time())
    indice_aleatorio = tempo_atual % tamanho_lista
    escolha = lista[indice_aleatorio]
    return escolha


minha_lista = [1, 2, 3, 4, 5]
resultado = escolha_aleatoria(minha_lista)
print(resultado)
