#Manejando series en Pandas
import pandas as pd
import numpy as np
ventas=pd.Series([20,30,50],index=["Enero","Febrero","Marzo"])
print(ventas)
print(ventas[1])
print(ventas["Enero"])
#con diccionario
datos={
    'a':1,
    'b':2,
    'c':3
    }
i=pd.Series(datos)
print(i)