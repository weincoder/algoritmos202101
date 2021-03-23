listaNombres = ['karla', 'Arturo', 'lauras','Juan']
print('karla' in listaNombres)

encontro = False
busqueda = 'mafer'
for elemento in listaNombres :
    if elemento == busqueda:
        encontro = True

print (encontro)
print(listaNombres.index('mafer'))
posicion = None
for i in range (len (listaNombres)):
    if listaNombres[i] == busqueda:
        posicion = i
print(posicion)