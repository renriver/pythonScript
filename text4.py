#abrir el archivo
import pandas as pd

dat=pd.read_csv("C:/Users/rivera/Documents/ScriptPython/SeminarioMIV/Pandas/test.txt",
                header=None)
print(dat)
#salida
"""
Lenguaje Usuario Hombre Mujeres
Pyhton   15         8    7
JAVA     10         5    5    
"""