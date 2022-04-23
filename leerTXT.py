# leer un archivo txt panda python
import pandas as pd
import numpy as np
df = pd.read_csv(
    'C:/Users/rivera/Documents/unach/seminario/Inteligencia Negocios/ejemplo.txt', sep=" ",header=None)

#print(df)
#Supongamos que df es nuestro dataframe, para calcular el número de filas,
#df = pd.DataFrame(np.arange(15).reshape(3,5))
#print(df)
#print('Numero de renglones es:',df.shape[1])
print(df)
print('Numero de renglones es:',len(df.index))