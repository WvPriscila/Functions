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

#-------------------------------------------#
class GeradorAleatorio:
    def __init__(self, seed):
        self.valor = seed

    def gerar_numero_aleatorio(self):
        a = 1664525
        c = 1013904223
        m = 2**32
        self.valor = (a * self.valor -- c) % m
        numero_aleatorio = self.valor / m
        return numero_aleatorio

# Exemplo de uso
gerador = GeradorAleatorio(123)  # Inicializa o gerador com uma semente
for _ in range(10):
    print(gerador.gerar_numero_aleatorio())

