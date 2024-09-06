#La funcion range toma dos argumentos y devuelve una lista que contiene todos
#los datos enteros entre el primero y el segundo, inclutyendo el primero pero
#no el segundo.

#range(10)
#[0,1,2,3,4,5,6,7,8,9]


#Lista vacia:
#No contiene elementos y se representa con []
#Ejemplo
'''
vocabulario = ["mejorar","castigar","defenestar"]
numeros = [17,123]
vacio = []
print(vocabulario, numeros, vacio)
'''
#Ubicar
'''
numeros2 = [1,2,45,67,34,2,4,5]
print (numeros2[4-1])
'''
#Usar variable de bucle para hacer lista:
'''
jinetes = ["guerra","hambre","peste", "muerte"]
i=0
while i<4:
#Tambien puede escribirse como i<len(jinetes)
    print(jinetes[i])
    i=i+1
'''
#Anidacion de listas:
lista = ['spam!',1,['Brie','Roquefort','Pol le Veq'],[1,2,3]]
i=0
while i<len(lista):
    print (f"la longitud de {lista[i]} es = {len(lista[i])}\n")
    i=i+1
