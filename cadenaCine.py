edad = int(input())

if edad < 4:
    print("Entrada gratis")
elif edad >= 4 and edad <= 12:
    print("Entrada infantil","precio $40")
elif edad >=13 and edad <=59:
        print("Entrada General","precio $70")
else :
        print("Entrada Adulto Mayor","precio con descuento del 35%")