import pandas as pd
import glob
import numpy as np
all_files = glob.glob("Aemet2019-*.xls")

file_list = []
for f in all_files:
    data = pd.read_excel(f,skiprows=4)
    data['origen'] = f # nueva columna conteniendo el nombre del fichero leido
    file_list.append(data)
    all_files 
df = pd.concat(file_list)
print(df.shape)
print(df.head())

