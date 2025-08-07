'''
Ejemplos de como implementar un ciclo en python'''

#Muestra la serie numérica de los primeros 10 número
print("Primer ciclo")
for i in range(10): #Rango del 0---9
    print(i)

#muestra los número del 1 al 5
print("Segundo ciclo")
for i in range(1, 6): #Ya no imprime cuando llega 6, el rango es 6 -1
    print(i)

#Muestra la serie numérica del 1 al 20 con incrementos de 2 en 2
print("Tercer ciclo")
for i in range(1,20,2):
    print(i)