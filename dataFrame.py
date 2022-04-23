#dataFrame o marco de datos
#tabla estructura bidimensional
#renglones, columnas
#   Registro | Nombre  | Valor
#    1       | Diego   | 8
#    2       | Jazhiel | 10 
#    3       | Romey   | 9.2
#    4       | Julian  | 6.7
#pandas
#p.DataFrame(data,index,columns,dtype,copy)
#crear un DataFrame vacio
import pandas as pd

#pand=pd.DataFrame()
#print(pand)
datos=[['Diego',8],['Jazhiel',10],['Romey',9]]
p=pd.DataFrame(datos,columns=['Nombre','Calificacion'])
print(p)