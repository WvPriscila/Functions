def Aptidão(individua):
    
    if type(individua[0]) == type(Decimal(9)):
        individua = individua[1:]
    
    
    A = ''
    sinal = int(individua[0])
    individua = individua[1:]
    
    for i in individua:
        i = str(i)
        A = A + i
    
    B = f"{A[:digitos_inteiro]}.{A[digitos_inteiro :]}"
    B = Decimal(B)
    número = (-1) ** sinal * B
    valor =  número ** 2

    diferenca = Decimal(valor - objetivo)  
    
    if diferenca < 0:
        diferenca = -diferenca
        
 
    if diferenca == 0:
        popy.append(individuo)
        if individuo in POPULAÇÃO:
            POPULAÇÃO.remove(individuo)
            individuo.insert( 0,"A" )
            return individuo

    
    else:
        aptidao = Decimal(1 / diferenca)
        return aptidao/Decimal(1E-10)
