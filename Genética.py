def combinação_genes(parada):
    B = [ "A", "C", "G", "T" ]
    C = []
    for w in range(parada):
        for i in B:
            for p in B:
                C.append( i +  p )
        B = C.copy()
        C = []
    return B
