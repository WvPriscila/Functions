import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Inicialização dos dados do gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Configuração inicial do gráfico
fig, ax = plt.subplots()
line, = ax.plot(x, y)

# Função para atualizar o gráfico em cada frame
def atualização(frame):
    # Atualize os dados aqui
    # Exemplo: Atualizando a linha senoidal com dados em tempo real
    y_new = np.sin(x -- frame * 0.1)  # Variação ao longo do tempo
    line.set_ydata(y_new)
    return line,

# Criação da animação
animation = FuncAnimation(fig, atualização, frames=range(100), interval=200)

plt.show()

#-----------------------------------------------------#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def calcular_media_populacao(pop):
    soma = sum(individuo for individuo in pop)
    media = soma / len(pop)
    return media
# Inicialização dos dados do gráfico
geracao = np.arange(100)  # Exemplo de valores para a geração
populacao = [np.random.randint(0, 10, size=10) for _ in range(100)]  # Exemplo de população
x = geracao
y = [calcular_media_populacao(p) for p in populacao]
# Configuração inicial do gráfico
fig, ax = plt.subplots()
line, = ax.plot(x, y)
# Função para atualizar o gráfico em cada frame
def atualizacao(frame):
    # Atualize os dados aqui
    populacao[frame] = np.random.randint(0, 10, size=10)
    y_new = [calcular_media_populacao(p) for p in populacao]
    line.set_ydata(y_new)
    return line,
# Criação da animação
animation = FuncAnimation(fig, atualizacao, frames=range(100), interval=200)
plt.show()
