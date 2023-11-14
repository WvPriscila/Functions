def selecionar_elementos_aleatorios(matriz_transposta):
    elementos_selecionados = []

    # Percorre cada lista na matriz transposta e seleciona um elemento aleatório
    for lista in matriz_transposta:
        if lista:
            elemento_selecionado = random.choice(lista)
            elementos_selecionados.append(elemento_selecionado)

    return elementos_selecionados
