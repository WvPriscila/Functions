A = [1, 4, 7, 9, 10, 11]
B = [2, 9, 8, 9, 11, 10]

for i, (a, b) in enumerate(zip(A, B)):
    if i % 2 == 0 and a == b:
        print(f"O elemento {a} é igual ao elemento {b} na posição {i} de ambas as listas.")

#------------------------
def contar_zeros_apos_virgula(numero):
    texto_numero = str(numero)
    encontrou_numero_diferente_de_zero = False
    contador_zeros = 0

    # Verifica se há uma parte decimal no número
    if '.' in texto_numero:
        parte_decimal = texto_numero.split('.')[1]

        # Procura o primeiro dígito diferente de zero após a vírgula
        index = parte_decimal.find('1')
        if index == -1:
            # Caso não encontre um dígito diferente de zero, todos os dígitos são zeros
            contador_zeros = len(parte_decimal)
        else:
            contador_zeros = index

    return contador_zeros

# Exemplo de uso
numero = 0.0000012300400
zeros_apos_virgula = contar_zeros_apos_virgula(numero)
print("Número de zeros após a vírgula:", zeros_apos_virgula)

#------------------------

A = [1, 4, 7, 9, 10, 11]
B = [2, 9, 8, 9, 11, 10]

for i in range(len(A)):
    if i % 2 == 0 and A[i] == B[i]:
        print(f"O elemento {A[i]} é igual ao elemento {B[i]} na posição {i} de ambas as listas.")


#---------------

A = [1, 4, 7, 9, 10, 11]
B = [2, 9, 8, 9, 11, 10]

for i in range(0, len(A), 2):
    if A[i] == B[i]:
        print(f"O elemento {A[i]} é igual ao elemento {B[i]} na posição {i} de ambas as listas.")

