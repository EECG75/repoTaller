promedio = 0
calificacion = 0
suma = 0
i = 0

calificacion = int(input("Escribe calificacion"))
if calificacion < 0:
    print("Numero de calificaciones",i)
    print("Promedio",promedio)
    
else:
    i = 1
    while calificacion >= 0:
        suma = suma + calificacion
        i+=1
        calificacion = int(input("Escribe calificacion"))
    i = i - 1
    promedio = suma / i
    print("El numero de calificaciones ingresadas fueron...", i)
    print("El promedio es....", promedio)

#Para romper un ciclo exit(), es igual al break()