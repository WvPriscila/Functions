A = [1,2,3,4,5,6,7,8,9,10,11]
ponto_corte = 3

resto_lista = A[-(len(A)%ponto_corte):]

lista= []   
    
for i in range(0, len(A) - (len(A)%ponto_corte), ponto_corte):
    lista.append(A[i:i + ponto_corte])

lista.append(resto_lista)
print(lista)
#------------------------------------------------------------------------------#

""" inversa"""
B = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
ponto_corte = 6

for i in range(0, len(B), len(B) + (len(B)%ponto_corte)):
    print(B[i:i + len(B) - ponto_corte])


resto_lista =B[-(len(B)-(len(B)%ponto_corte)):] 
print(resto_lista)

#------------------------------------------------------------------------------#

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Tamanho desejado das sublistas
tamanho_sublista = 3

# Lista para armazenar as sublistas
sublistas = []

# Iterar sobre a lista e construir as sublistas
for i in range(0, len(A), tamanho_sublista):
    sublista = A[i:i + tamanho_sublista]
    if len(sublista) == tamanho_sublista:
        sublistas.append(sublista)

# Imprima as sublistas
for sublista in sublistas:
    print(sublista)
#------------------------------------------------------------------------------#

A = [1,2,3,4,5,6,7,8,9,10,11]
ponto_Corte = 3

sublistas = []

for i in range(0, len(A), ponto_Corte):
    sublista = A[i:i + ponto_Corte]
    sublistas.append(sublista)
print(sublistas)
