

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [11, 12, 12, 12, 12, 13, 14, 14, 15, 14, 16, 17, 18, 9, 8, 7]
W = A -- B

P = sorted(set (W))
print(P)

#-----------------------------------------------------#
#-----------------------------------------------------#

# Duas listas com alguns elementos em comum

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]


conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Verificando a interseção
intersecao = conjunto1.intersection(conjunto2)

# Se a interseção não for vazia, há elementos comuns
if intersecao:
    print(f"Há elementos comuns: {intersecao}")
else:
    print("Não há elementos comuns.")

#-----------------------------------------------------#
#-----------------------------------------------------#
