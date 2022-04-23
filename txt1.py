#manejo de archivos de texto plano
#read_csv() cargar archivos de texto
#read_fwf() cargar archivos de texto pero en formato panda dataframe
#read_table() cargar el archivo de texto a panda en dataframe
import pandas as pd

#dato= pd.read_csv("ruta_archivo",delimitacion,encabezado)
info= pd.read_csv('C:/Users/rivera/Documents/ScriptPython/SeminarioMIV/Pandas/test.txt',
                 sep=",",header=None)

print(info)
#manejando datos read_fwf()
info=pd.read_fwf('C:/Users/rivera/Documents/ScriptPython/SeminarioMIV/Pandas/test.txt',
                delimiter=",")
print(info)
#read_table()
info=pd.read_table('C:/Users/rivera/Documents/ScriptPython/SeminarioMIV/Pandas/test.txt',
                   sep=",",header=None)
print(info)
