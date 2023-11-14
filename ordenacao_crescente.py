def ordenacao_crescente(lista):
    lista_ordenada = []
    while lista:
        menor_elemento = encontrar_menor_elemento(lista)
        lista_ordenada.append(menor_elemento)
        lista.remove(menor_elemento)
    return lista_ordenada
