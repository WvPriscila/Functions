def ordenacao_decrescente(lista):
    lista_ordenada = []
    while lista:
        maior_elemento = encontrar_maior_elemento(lista)
        lista_ordenada.append(maior_elemento)
        lista.remove(maior_elemento)
    return lista_ordenada
