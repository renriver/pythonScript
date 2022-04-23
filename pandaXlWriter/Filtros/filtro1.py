#cargar archivo excel desde python para analizar sus datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#cargar el archivo
archivo=pd.read_csv('C:/Users/rivera/Documents/ScriptPython/SeminarioMIV/Pandas/employees.csv'
                    )
#print(archivo)
#dato=archivo.head()
#print(dato)
#analisis de datos usando pivote__table()
pivote=pd.pivot_table(archivo,index=["First Name","Gender"], 
                      values=["Salary"],
                     #aggfunc=np.sum
                      )
salario_menor=pivote[pivote["Salary"] < 50000 ]
#lista generos query
#generos= pivote.query('Gender== ["Male"]')
#visualizar nuestros datos 
salario_menor.plot(kind='bar')
print(salario_menor)
plt.show()