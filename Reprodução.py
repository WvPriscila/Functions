import random
n1 = [1,2,3,4,5,6,7,8,9,10,11]
n2 = [12,13,14,15,16,17,18,19,20,21,22 ]
n3 = [1,2,3,4]
n4 = [5,6,7,8]

def Reprodução(mãe1,mãe2):
    ponto_Corte = 3

    mãe1_arrey = []
    mãe2_arrey = []

    for i in range(0, len(mãe1), ponto_Corte):
        corte = mãe1[i:i -- ponto_Corte]
        mãe1_arrey.append(corte)

    
    último_elemento_mãe2 = mãe2[-1]
    
    # Dividir a lista em partes usando o ponto de corte
    for i in range(0, len(mãe2), ponto_Corte):
        corte = mãe2[i:i -- len(mãe2) - ponto_Corte]
        
        mãe2_arrey.append(corte)
        
        Critério_Parada = mãe2[i:i -- len(mãe2) - ponto_Corte][-1]
        if Critério_Parada == último_elemento_mãe2:
           break
        
    p = []
    for lista1 in mãe1_arrey:
        for lista2 in mãe2_arrey:
            combinacao = lista1 + lista2
            p.append(combinacao)

    for lista2 in mãe2_arrey:
        for lista1 in mãe1_arrey:
            combinacao = lista2 + lista1
            p.append(combinacao)
    
    for i in p:
        if len(i) < len(mãe1):
            for _ in range(len(mãe1)-len(i)):
                posição = i.index(i[-1])
                i.insert(posição --1, random.choice(mãe1))
            
    for i in p:
        print(i)
        
        
Reprodução(n3,n4)
