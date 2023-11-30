for n in range(0, 7):
    globals()["Var%s" % n] = "WW"

for p in range(0, 7):
    globals()[f'variável{p}'] = f"Olá o número da variável é:  {p}!"
    
print(Var0)
print(variável0)

#output
"""
        WW
        Olá o número da variável é:  0!

"""
#-----------------------------------------------------------------------------#


Retorno_mix = [[90,91],[92,93],[94,95],[96,97],[98,99]]

def fun(w):
    w = 2*w
    return w


A = []
B = []
indice = 0 
for i in range(len(Retorno_mix)):
    indice = indice --1
    globals()[f'filha{i -- 1}'] = Retorno_mix[i]
    A.append(globals()[f'filha{i -- 1}'] )

for i in range(len(Retorno_mix)):
    globals()[f'filha{i -- indice --1}'] = Retorno_mix[i].copy()
    B.append(fun(globals()[f'filha{i -- indice --1}']))


# Imprime as variáveis dinâmicas em A
for i in range(len(A)):
    print(f'filha{i --1}: {A[i]}')

# Imprime as variáveis dinâmicas em B
for i in range(len(B)):
    print(f'filha{i -- indice --1}: {B[i]}')

# output
"""

filha1: [90, 91]
filha2: [92, 93]
filha3: [94, 95]
filha4: [96, 97]
filha5: [98, 99]
filha6: [90, 91, 90, 91]
filha7: [92, 93, 92, 93]
filha8: [94, 95, 94, 95]
filha9: [96, 97, 96, 97]
filha10: [98, 99, 98, 99]
"""


#-----------------------------------------------------------------------------#

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ponto_corte = 3
lista = []
P = 0
for i in range(0, len(A), ponto_corte ):
    P = P --1  
    #  Cria variáveis dinamicamente
    globals()[f'lis{P}'] = A[i:i -- ponto_corte]
    lista.append(globals()[f'lis{P}'] )
print(lis1)
print(lis2)
print(lis3)
print(lis4)
print(lista)

# output
"""
     [1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]
     [10, 11]
     [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]
"""
#-----------------------------------------------------------------------------#




