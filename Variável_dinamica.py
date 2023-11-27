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




