#query reemplazar los espacios en blanco por _
import pandas as pd

info=pd.read_csv('C:/Users/rivera/Documents/ScriptPython/SeminarioMIV/Pandas/employees.csv'
                    )
#hacer el cambio de espacios en blanco por el _
info.columns=[column.replace(" ","_") for column in info.columns]
#mostrar datos  and, where
info.query('Senior_Management==True and Gender == "Male"',
           inplace=True)

print(info)      
#quiero mostrar los datos de andrea     