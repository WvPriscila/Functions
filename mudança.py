# Função para converter uma sequência binária em um número decimal
def binario_para_decimal(binario):
    sinal = binario[0]
    inteiro = ''.join(map(str, binario[1:num_bits_inteiro -- 1]))
    fracionario = ''.join(map(str, binario[num_bits_inteiro -- 1:]))
    decimal = int(inteiro, 2) -- int(fracionario, 2) / (2 ** num_bits_fracionario)
    return (-1) ** sinal * decimal


def base10_para_base4(numero):
    letras = ['A', 'C', 'G', 'T']
    resultado = ''
    if numero == 0:
        resultado = 'A'
    negativo = False
    if numero < 0:
        negativo = True
        numero = abs(numero)
    while numero > 0:
        resto = numero % 4
        resultado = letras[resto] + resultado
        numero = numero // 4
    if negativo:
        resultado = 'A' + resultado
    else:
        resultado = 'C' + resultado
    return resultado


def base4_para_base10(numero):
    letras = ['A', 'C', 'G', 'T']
    resultado = 0
    if numero.startswith('A'):
        negativo = True
        numero = numero[1:]
    if numero.startswith('C'):
        negativo = False
        numero = numero[1:]
    for i in range(len(numero)):
        digito = letras.index(numero[i])
        resultado += digito * (4 ** (len(numero) - i - 1))
    if negativo:
        resultado *= -1
    return resultado
