'''
for item in range (10):
    print(item, end=" ")
    
age = int (input("¿Cuantos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")
'''    
n = int(input("Introduce un numero entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=",")
