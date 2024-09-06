'''
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

Edad = int(input("Escribe tu edad"))
if Edad > 18:
     print("Eres mayor de edad")
else:
     print("Eres menor de edad")

#Escribir un programa que al ususario dos numeros y muestre en pantalla la divisióm, si el divisor es 0 el progrema debera mostrar un error"


n1 = int(input("Proporciona el primer valor"))
n2 = int(input("proporciona el segundo valor"))
if n2 == 0:
    print ("Su division no es posible")
else:
    print("El resultado es:", n1/n2)

#Escribir un programa que pida al usuario un numero entero y muestre en pantalla si es par o impar

entero = int (input("Introduce un numero entero: "))
if entero % 2 == 0:
    print("El numero " + str(entero) + " es par")
else:
    print("El numero " + str(entero) + " es impar")

'''
