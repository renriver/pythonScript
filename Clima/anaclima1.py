#vamos a cargar esos datos en una variable
#arreglos
import pandas as pd
import numpy as np
import glob
#abrir mis archivos
archivos=glob.glob("Aemet2014-*.xls")#ruta de los ficheros/archivos
#cargar nuestro datos
lista_archivo=[]

for f in archivos:
    informacion=pd.read_excel(f,skiprows=4)
    informacion['origen']=f #una nueva columna donde va el nombre de cada archivo leido
    lista_archivo.append(informacion)
datos=pd.concat(lista_archivo)
#print(datos)
#pro=datos.groupby('Provincia').mean()
#print(pro)
#renombrar las columnas
datos=datos.rename(columns={'Estacion':'estacion', 'Provincia':'provincia',
                            'Temperatura máxima (ºC)':'temp_max', 'origen':'fecha'})
#print(datos.head(1))
#imprimir las temperatura mas altas del mes
temp_max=datos.sort_values(by='temp_max', ascending=False)[['fecha','provincia','temp_max']].head(3)
print(temp_max)     