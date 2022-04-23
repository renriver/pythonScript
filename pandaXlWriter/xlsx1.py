import xlsxwriter 
  
workbook = xlsxwriter.Workbook('hola.xlsx') 
  
worksheet = workbook.add_worksheet() 
  
worksheet.write('A1', 'H') 
worksheet.write('B1', 'G') 
worksheet.write('C1', 'R') 
worksheet.write('D1', 'J') 
  
workbook.close() 
