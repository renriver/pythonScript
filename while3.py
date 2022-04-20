#calcule el promedio de calificaciones de alumno
suma=0
aux=0
print("ingrese una calificacion")
print("si desea salir digite -1")
cal=int(input())#introducir por teclado
while (cal != -1):
    suma=suma+cal
    aux=aux+1
    print("ingrese una calificacion(-1 para salir del sistema)")
    cal=int(input())
promedio=suma/aux
print("Tu promedio es: ",promedio)