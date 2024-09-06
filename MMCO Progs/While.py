i = 0
'''
while i <=20:
    print (i)
    i+=2

while i<10:
    print (i,end=",")
    i = i+1
'''

continuar = True
while continuar:
    valor = int(input("Introduce un entero superior a 100: "))
    if valor>100:
        continuar = False
print ("Programa acabado")
