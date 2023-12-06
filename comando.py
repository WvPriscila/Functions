# Definindo uma função simples
def quadrado(x):
    return x * x

def cubo(x):
    return x * x * x

# Usando max() com uma função como parâmetro
resultado_max = max(5, 8, 12, key=quadrado)
print("Máximo usando quadrado:", resultado_max)

resultado_max_cubo = max(5, 8, 12, key=cubo)
print("Máximo usando cubo:", resultado_max_cubo)
