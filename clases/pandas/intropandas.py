import pandas as pd
listaVariada = ['a',1,2,4.6]
print (listaVariada)
seriesPandas = pd.Series ([1,2,5])
print (seriesPandas)
seriesPandas = pd.Series ([4.6,5.7,0.1])
print(seriesPandas)
dicGanancias = {}
dicGanancias['Enero'] = 4300
dicGanancias['Febrero'] = 4545
dicGanancias['Marzo'] = 2324
dicGanancias['Abril'] = 1244
seriesGananciaPorMes = pd.Series([4300,4545,2324,1244])
print (seriesGananciaPorMes)
seriesGananciaPorMesDic = pd.Series (dicGanancias)
print ('Enero', seriesGananciaPorMesDic['Enero'])
print (seriesGananciaPorMesDic['Enero':'Marzo'])
print (seriesGananciaPorMesDic['Febrero':'Marzo'])

matrizEstudiantes = [
                        ['Karla', 'Mario', 'Laura'],
                        ['Santi', 'Arturo', 'Vale'],
                        ['Juan', 'Melany', 'Laura'],
                        ['Mafer', 'Esteban'],
                    ]
dataFrameNombres = pd.DataFrame(matrizEstudiantes)

matrizEstudiantesDic = {
                        'Grupo1' :  ['Karla', 'Mario', 'Laura'],
                        'Grupo2' :  ['Santi', 'Arturo', 'Vale'],
                        'Grupo3' :  ['Juan', 'Melany', 'Laura'],
                        'Grupo4' :  ['Mafer', 'Esteban',None],
}
dataFrameNombres = pd.DataFrame(matrizEstudiantes)
dataFrameNombresDic = pd.DataFrame(matrizEstudiantesDic)
print (dataFrameNombres)
print (dataFrameNombresDic)
print ("#"*60)
print (dataFrameNombresDic['Grupo2'])
print ("#"*60)
print (dataFrameNombresDic['Grupo2'])
print ("#"*60)
print (dataFrameNombresDic)
print ("#"*60)
print (dataFrameNombresDic.iloc[1:])

dicVentasPorMes = {
    'Ene($)' :[1234,4235,2356],
    'Abril (millones de pesos)' :[1234,423342,223356],
    'Mayo (millones de pesos)'  :[4123,4537,6577]
}
print ("#"*60)
dataFrameVentas = pd.DataFrame (dicVentasPorMes, index = ['Tomates', 'Papa', 'Yuca'])
print (dataFrameVentas.iloc[2])