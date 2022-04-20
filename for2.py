#extraer una tupla de una lista de tuplas
tupla1=(1,"hola","mundo")
#anidar tuplas dentro de otra tupla
tupla_anidada=(2,"uno",(10,2022,"Año"))
tupla_anidad2=(tupla_anidada,tupla1,"Tres")
print(tupla_anidad2[1])
#para la longitud usar la funcion len()
print(len(tupla_anidad2))
