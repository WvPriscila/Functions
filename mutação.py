

def Possivel_mutação(individua):
    for i in range(len(individua)):
        if random.random() < taxa_mutacao:
            individua[i] = random.randint(0, 9)
    return individua


def mutação_Obrigatória(individua):
    for i in range(len(individua)):
        individua[i] = random.randint(0, 9)
    return individua




# Função para realizar a mutação em um indivíduo
def mutacao(individuo):
    for i in range(num_genes):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]



