def remove_repetidos(inteiros):

    lista = []

    for x in inteiros:
        if x not in lista:
            lista.append(x)
    return sorted(lista)
        
