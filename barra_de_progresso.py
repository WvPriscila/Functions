def exibir_barra_de_progresso(Ga, Gf):
    caracteres = ['|', '/', '-', '\\']
    while True:
        for char in caracteres:
            sys.stdout.write(f'\r{char} Porcentagem: {100 * (Ga / Gf):.1f}%')
            sys.stdout.flush()
            time.sleep(0.2)  # 0.2 segundos (200 milissegundos) para cada caractere

        break
