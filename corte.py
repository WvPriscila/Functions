A = [1,2,3,4,5,6,7,8,9,10,11]

ponto_corte = 3

resto_lista = A[-(len(A)%ponto_corte):]

lista= []   
    

for i in range(0, len(A) - (len(A)%ponto_corte), ponto_corte):
    lista.append(A[i:i + ponto_corte])

lista.append(resto_lista)
print(lista)


#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#


A = [1,2,3,4,5,6,7,8,9,10,11]
ponto_Corte = 3

numero_gene_perfeitamente_cortados = len(A) // ponto_Corte
numero_gene_imperfeitamente_cortado = len(A) % ponto_Corte

p = len(A) - (len(A) // ponto_Corte)

sublistas = []

for i in range(0, len(A), ponto_Corte):
    sublista = A[i:i + ponto_Corte]
    sublistas.append(sublista)
print(sublistas)
