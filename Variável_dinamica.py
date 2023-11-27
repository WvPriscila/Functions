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





