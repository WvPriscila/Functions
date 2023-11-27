A = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

ponto_Corte = 3

p = len(A) - ( len(A)//ponto_Corte)

for i in range(p):
    sublista = A[i:i + p]
    print(sublista)

    if i + p == len(A):
        break

# output
"""  
     [12, 13, 14, 15, 16, 17, 18, 19]
     [13, 14, 15, 16, 17, 18, 19, 20]
     [14, 15, 16, 17, 18, 19, 20, 21]
     [15, 16, 17, 18, 19, 20, 21, 22]

"""
