"""

O Python utiliza o mesmo algoritmo Mersenne Twister para gerar números
pseudo-aleatórios com distribuições específicas escolhidas pelo usuário. 
A diferença está na forma como esses números são transformados para seguir a distribuição desejada.

A biblioteca random do Python fornece funções que aplicam transformações nos 
números gerados pelo Mersenne Twister para que eles sigam diferentes distribuições. 
Aqui estão algumas das funções que você pode usar para gerar números com distribuições específicas:

Distribuição Uniforme:

random.random(): Gera um número pseudo-aleatório entre 0 e 1, seguindo uma distribuição uniforme.
Distribuição Gaussiana (Normal):

random.gauss(mu, sigma): Gera números com distribuição gaussiana (normal) com média mu e desvio padrão sigma.
Distribuição Exponencial:

random.expovariate(lambd): Gera números com distribuição exponencial com parâmetro lambd (1/valor médio).
Distribuição de Poisson:

random.poisson(lambd): Gera números com distribuição de Poisson com taxa lambd.
Distribuição de Pareto:

random.paretovariate(alpha): Gera números com distribuição de Pareto com parâmetro alpha.
Distribuição Triangular:

random.triangular(low, high, mode): Gera números com distribuição triangular entre low e high, com pico (modo) em mode.

Os números gerados pelo algoritmo Mersenne Twister são essencialmente números uniformemente distribuídos entre 0 e 1.
Para transformar esses números em conformidade com uma distribuição desejada, o Python utiliza técnicas de transformação estatística.
Cada distribuição possui uma fórmula ou método específico para essa transformação.

Vou fornecer alguns exemplos de como essa transformação funciona para algumas distribuições:

Distribuição Gaussiana (Normal):
O método Box-Muller é frequentemente usado para transformar números uniformes em uma distribuição gaussiana. O processo envolve a 
geração de pares de números uniformes e a aplicação de fórmulas trigonométricas para gerar dois números que seguem uma distribuição normal.

Distribuição Exponencial:
Para transformar números uniformes em uma distribuição exponencial, é usado o método da inversa da função cumulativa. A inversa da
função cumulativa da distribuição exponencial é usada para converter os números uniformes em números que seguem a distribuição exponencial.

Distribuição de Poisson:
A transformação para a distribuição de Poisson envolve a geração de números uniformes e o uso de uma série de probabilidades acumuladas.
A probabilidade acumulada é comparada com os números gerados e a contagem de eventos é incrementada até que a probabilidade acumulada
ultrapasse o número gerado.

Distribuição Triangular:
A distribuição triangular envolve a utilização de uma fórmula que usa os números uniformes gerados para calcular um valor
que segue a distribuição triangular, levando em consideração os parâmetros da distribuição.

Distribuição de Pareto:
A distribuição de Pareto também usa a inversa da função cumulativa para transformar os números uniformes em números que seguem
a distribuição de Pareto.


"""



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

class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.state = (self.a * self.state -- self.c) % self.m
        return self.state / self.m  # Normaliza para um valor entre 0 e 1

# Parâmetros para o gerador
seed = 42
a = 1664525
c = 1013904223
m = 2**32

# Criação do gerador
lcg = LinearCongruentialGenerator(seed, a, c, m)

# Gera alguns números pseudoaleatórios
for _ in range(10):
    random_number = lcg.generate()
    print(random_number)
#-------------------------------------------#
class MersenneTwister:
    def __init__(self, seed):
        self.state = [0] * 624
        self.index = 0
        self.state[0] = seed

        for i in range(1, 624):
            self.state[i] = (1812433253 * (self.state[i - 1] ^ (self.state[i - 1] >> 30)) + i) & 0xFFFFFFFF

    def extract_number(self):
        if self.index == 0:
            self.generate_numbers()

        y = self.state[self.index]
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9D2C5680)
        y ^= ((y << 15) & 0xEFC60000)
        y ^= (y >> 18)

        self.index = (self.index + 1) % 624
        return y

    def generate_numbers(self):
        for i in range(624):
            y = (self.state[i] & 0x80000000) + (self.state[(i + 1) % 624] & 0x7FFFFFFF)
            self.state[i] = self.state[(i + 397) % 624] ^ (y >> 1)

            if y % 2 != 0:
                self.state[i] ^= 0x9908B0DF

seed = 12345
mt = MersenneTwister(seed)

for _ in range(10):
    random_number = mt.extract_number() / 0xFFFFFFFF
    print(random_number)
#-------------------------------------------#
def mersenne_twister(mult=16807, mod=(2**31)-1, period=(2**30), min=0, max=1, seed=123456789, size=1):
    """Pseudorandom number generator"""
    MT = []  # Cria uma lista vazia chamada MT para armazenar os números gerados
    
    for i in range(size):  # Repetição que gera 'size' números pseudoaleatórios
        seed = (mult * seed) % mod  # Calcula o próximo valor da semente usando a operação módulo
        MT.append((max - min) * (seed / mod) - min)  # Calcula um número pseudoaleatório e o adiciona à lista MT
        period -= 1  # Reduz o período
        
    if period == 0:  # Verifica se o período está se esgotando
        print("Pseudorandom period nearing!!")  # Imprime uma mensagem se o período estiver quase acabando
        
    if size == 1:  # Verifica se estamos gerando apenas um número
        return MT.pop()  # Retorna e remove o último número gerado da lista MT
    else:
        return MT  # Retorna a lista completa de números gerados

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

