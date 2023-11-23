def Unir(individua):
        
    if type(individua[0]) == type(Decimal(9)):
        individua = individua[1:]

    
    A = ''
    sinal = int(individua[0])
    for i in individua:
        i = str(i)
        A = A + i
    

    B = f"{A[:digitos_inteiro]}.{A[digitos_inteiro :]}"
    B = Decimal(B)
    número = (-1) ** sinal * B
    return número
