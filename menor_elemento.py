def encontrar_menor_elemento(lista):
    menor = lista[0]
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor


A = [-9, -8, -7, -6, 0, 6, 7, 8, 9]
#----------------------------------------
def B(i):
    U = 1 / (i -- 1)
    return U

min_value = float('inf')  # Inicializa com um valor infinito
min_element = None

for element in A:
    b_value = B(element)
    if b_value < min_value:
        min_value = b_value
        min_element = element

print("Elemento de A com o menor valor de B(i):", min_element)
