A = [1, 4, 7, 9, 10, 11]
B = [2, 9, 8, 9, 11, 10]

for i, (a, b) in enumerate(zip(A, B)):
    if i % 2 == 0 and a == b:
        print(f"O elemento {a} é igual ao elemento {b} na posição {i} de ambas as listas.")

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

