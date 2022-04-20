#break --> detiene una iteracion en ejecucion
#continue -->detiene una iteracion actual y va pasar a la siguiente
# 
x=0
while (x<10):
    x=x+1
    if(x==5):
        continue
    print(x)
#break
print("Usando Break")
y=0
while(y<10):
    y=y+1
    print(y)
    if(y==5):
        break
