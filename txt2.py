import pandas as pd
 
dato=pd.read_csv('C:/Users/rivera/Documents/ScriptPython/SeminarioMIV/Pandas/test.txt'
                  ,sep=",", header=None,names=["A","B","C","D","F"])
print(dato)