#iteraciones sobre una lista o tupla
valores=["hola",10,50,"mundo",[1,2]]
#iterar sobre esa lista usando un for  in
for x in valores:
    print(x)
#trabajar sobre diccionarios usando for
print("Iteraciones sobre un diccionario")
dic={
    'uno':1, 
    'dos':2,
    'tres':3
    }
for x in dic:
    print(x)
#usando la funcion values()
print("Usando el metodo values() ")
for x in dic.values():
    print(x)
#conocer iterar sobre los valores y claves de un diccionario metodo items()
print("Usando el metodo items() ")
for x,id in dic.items():
    print(x,id)
