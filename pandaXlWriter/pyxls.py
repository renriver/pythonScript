#python pueden crear o escribir archivos de excel
#xlsxwriter libreria de python formato xlsx archivos de excel
#graficas, imagenes, filtro, entre otros.
#instalara libreria xlsxwriter 
#pip install xlsxwriter
#crear un archivo de excel desde python
import xlsxwriter

archivo=xlsxwriter.Workbook("archivo1.xlsx")
#hojas libro archivo de excel
hoja=archivo.add_worksheet()
#agregar datos
hoja.write('A1','Nombre')
hoja.write('B1','Apellido')
hoja.write('C1','Telefono')
#manejo de contenido en filas y las columnas
#row, column
row=1
column=0
#informacion en el archivo 
info=["Rene","Luis","Bersai","Julian","Alexis"]
for i in info:
    hoja.write(row,column,i)
    row+=1

#cerrar el archivo
archivo.close()


