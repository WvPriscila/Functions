def calcular_total_aptidao(populacao):
    total_aptidao = 0
    for individuo in populacao:
        total_aptidao += Decimal(Aptidão(individuo))
    return total_aptidao
