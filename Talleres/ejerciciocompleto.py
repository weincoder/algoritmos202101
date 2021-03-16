# Crear un elemento donde muestre las ventas totales mes a mes
# de una empresa durante un año
import pandas as pd
dicEarningsPerYear = {}
dicEarningsPerYear['Enero'] = 1234124
dicEarningsPerYear['Febrero'] = 323212
dicEarningsPerYear['Marzo'] = 1234432124
dicEarningsPerYear['Abril'] = 1232344124
dicEarningsPerYear['Mayo'] = 123434124
dicEarningsPerYear['Junio'] = 1231234124
dicEarningsPerYear['Julio'] = 123544124
dicEarningsPerYear['Agosto'] = 123443124
dicEarningsPerYear['Septiembre'] = 123443124
dicEarningsPerYear['Octubre'] = 123443124
dicEarningsPerYear['Noviembre'] = 123443124
dicEarningsPerYear['Diciembre'] = 123443124
serieEarningsPerYear = pd.Series(dicEarningsPerYear)
print (serieEarningsPerYear)
#Muestren en pantalla las ganancias por trimestre
print ('primer trimeste')
print(serieEarningsPerYear['Enero':'Marzo'])
print ('tercer trimeste')
print(sum( serieEarningsPerYear['Julio':'Septiembre']))
dicGananciasTrimestrales = {}
dicGananciasTrimestrales['1er Trimestre'] = sum (serieEarningsPerYear['Enero': 'Marzo'])
dicGananciasTrimestrales['2do Trimestre'] = sum (serieEarningsPerYear['Abril': 'Junio'])
dicGananciasTrimestrales['3er Trimestre'] = sum (serieEarningsPerYear['Julio': 'Septiembre'])
dicGananciasTrimestrales['4to Trimestre'] = sum (serieEarningsPerYear['Octubre': 'Diciembre'])
seriesGananciasTrimestrales = pd.Series(dicGananciasTrimestrales)
print (seriesGananciasTrimestrales)
print (sum(serieEarningsPerYear))
#Gancias por mes por Departamento Antioquia, Amazones, Cundinamarca
dicGananciasPorDepartamento = {
    'Antioquia': [124343,3554354,453435,45314,435453,543445],
    'Amazonas': [124342343,3554354,453234435,45313214,435453,543445],
    'Cundinamarca': [12432343,4354,4535,454,4354,543]
}
listaMeses = ['Enero', 'Febrero', 'Marzo', 'Abril','Mayo','Junio']
dataFrameGananciasPorDepartamento = pd.DataFrame(dicGananciasPorDepartamento, index= listaMeses)
print (dataFrameGananciasPorDepartamento)

print (dataFrameGananciasPorDepartamento[['Antioquia','Amazonas']]['Febrero':'Abril'])