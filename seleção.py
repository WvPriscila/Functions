def seleção(populção):
    total_aptidão = calcular_total_aptidao(populção)
    escolhido = random.uniform(0, float(total_aptidão))  # Convertendo para float
    acumulado = 0

    for individuo in populção:
        aptidão_individuo = Aptidão(individuo)
        acumulado += aptidão_individuo

        if acumulado >= escolhido:
            return individuo



# Função para selecionar dois indivíduos para reprodução (roleta viciada)
def selecao(populacao):
    total_Aptidão = sum(Aptidão(individuo) for individuo in populacao)
    roleta = []
    for individuo in populacao:
        Aptidão_individuo = Aptidão(individuo)
        probabilidade = Aptidão_individuo / total_Aptidão
        roleta.extend([individuo] * round(probabilidade * 100))
    return random.choice(roleta)


def seleção(populção):
    total_aptidao = 0
    
    for individuo in populção:
        apt = Aptidão(individuo) 
        if type(apt) == type(["A"]):
            continue
        else:
            total_aptidao = total_aptidao + Decimal(Aptidão(individuo))

    total_aptidao = float(total_aptidao)  # Convertendo para float

    escolhido = random.uniform(0, total_aptidao) 
    acumulado = 0

    for individuo in populção:
    
        
        aptidão_individuo = Aptidão(individuo)
        
        if type(aptidão_individuo) == type(["A"]):
            continue
        
        else:
        
            acumulado += aptidão_individuo
            if acumulado >= escolhido:
                return individuo
