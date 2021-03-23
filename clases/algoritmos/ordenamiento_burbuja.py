
def ordenamientoBurbuja(listaEntrada = [] ):
    sizeList = len (listaEntrada)
    for i in range(sizeList):
        for j in range (sizeList-1):
            if (listaEntrada[j]>listaEntrada[j+1]):
                listaEntrada[j+1], listaEntrada[j] = listaEntrada[j], listaEntrada[j+1]
    return listaEntrada


