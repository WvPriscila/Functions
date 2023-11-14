def Unir_digitos(lista):
    A = ''
    # print("lista",lista)
    sinal = int(lista[0])
    for i in lista:
        i = str(i)
        A = A + i

    B = f"{A[1:digitos_inteiro + 1]}.{A[digitos_inteiro + 1:]}"

    número = (-1) ** sinal * Decimal(B)
    return número
