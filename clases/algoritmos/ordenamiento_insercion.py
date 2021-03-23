
def ordenamientoInsercion(lista):
    ''' Se ordena una lista 
    utilizando el méto de inserción
    '''
    for indice in range (1, len(lista)):
        valorActual = lista[indice]
        posicionActual = indice
        while (posicionActual>0 and lista[posicionActual-1]> valorActual):
            lista[posicionActual] = lista[posicionActual -1]
            posicionActual -=1
        lista[posicionActual] = valorActual
    return lista

