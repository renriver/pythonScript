#formato a nuestro archivos
#.set_column() tamaño en columnas, 
# set_row() tamaño en filas
# 
import xlsxwriter
import pandas as pd
archivo=xlsxwriter.Workbook("Archivo2.xlsx")

hojas=archivo.add_worksheet()

hojas.write('A1','')
hojas.write('B1','')
hojas.write('C1','')
hojas.write('D1','')
#columnas
hojas.set_column('B:B',20)
#filas/renglones
hojas.set_row(0,50)
#formatos
formato_titulo=archivo.add_format({
    'bold':1,
    'border':1,
    'align':'center',
    'valign':'vcenter',
    'fg_color':'blue',
    'font_color':'white',
    'text_wrap':True
    
})

#.merge_range() combinacion de filas y columnas en un rango en una sola celda

hojas.merge_range('B1:D1','lista de alumnos',formato_titulo)
#fila2
hojas.write('B2','codigo')
hojas.write('C2','id codigo')
hojas.write('D2','Algo')



archivo.close()