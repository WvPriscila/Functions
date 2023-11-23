def inicializar_populacao():
    for i in range(tamanho_população_inicial):
        individua = [random.randint(0, 9) for i in range(num_genes)]
        POPULAÇÃO.append(individua)
    return POPULAÇÃO


def inicializar_populacao(POPULAÇÃO):
    
    POP = []
    for i in range(tamanho_população_inicial):
        individuo = [random.randint(0, 9) for i in range(num_genes)]
        individuo.insert(0,Aptidão(individuo))
        POP.append(individuo)
        
    return POP
