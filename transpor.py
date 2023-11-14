def transpor_matriz(matriz):
    # Verifica se a matriz está vazia
    if not matriz:
        return []

    # Encontra o número de linhas e colunas na matriz
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    # Inicializa a matriz transposta com listas vazias
    matriz_transposta = [[] for i in range(num_colunas)]

    # Preenche a matriz transposta com os elementos da matriz original
    for i in range(num_linhas):
        for p in range(num_colunas):
            matriz_transposta[p].append(matriz[i][p])

    return matriz_transposta
