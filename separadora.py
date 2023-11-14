def separadora(arrey):
    if len(arrey) % 2 == 0:
        indice = int(len(arrey) / 2)
    else:
        indice = int(len(arrey) // 2 - -1)

    return indice
