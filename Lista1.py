#lista datos compuestos
lista1=[2,4,6,8,10]
print(lista1)
#podemos indexar 
print(lista1[0])
print(lista1[-3])
print(lista1[:-3])
#concatenar otra lista
lista2=lista1+[1,3,5,7,9]
print(lista2)

cad="Python" #PytHon
print(cad[3])
#cad[3]="H"
#print(cad)
#lista

#lista2=[2,4,6,8,10,1,3,5,7,9] cambiar el 1 por el 11
lista2[5]=11
print(lista2)
#agregar elemento a la lista al final
#append()
lista2.append(15)
print(lista2) 
#dimension de lista
#len()
print(len(lista2))
#lista dentro de otra lista
numero=[1,2,3,4,5]
vocal=['a','e',30,'o','u']
mixta=[numero,vocal]
print(mixta)
