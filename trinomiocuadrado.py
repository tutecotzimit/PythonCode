#(x+y)^2=x^2+2xy+y^2
#Variables:
#x
#y
#Procesamiento
#trinomio=x**2+2*x*y+y**2
x=int(input("Escriba el primer término:"))
y=int(input("Escriba el segundo término"))
trinomio=(x**2) + (2*x*y) + (y**2)
print(f"El trinomio cuadrado perfecto para ({x} + {y})^2={trinomio}")