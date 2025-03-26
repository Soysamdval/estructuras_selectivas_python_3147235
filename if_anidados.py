'''
if anidados:
if dentro de otros if

sintax:
if condicion1:
    if condicion2:
        print("mensaje")
        if condicion3:
            print ("mensaje")
    else:
        print("mensaje")

no confundir con elif
'''

#ejemplo 1:

#Modifique el ejercicio de la edad
#para las siguientes condiciones
#1. si es mayor de 18 años
#pero no tiene documento, no puede votar
#de lo contrario si puede votar

#2. si es menor de 18 años 
#no puede votar

#utilice estructura de If anidados

edad = int(input("ingrese su edad: "))
if edad >= 18:
    documento = input ("¿tiene documento? (si/no): ")
    if documento == "si":
        print ("puede votar")
    else:
        print ("no puede votar")
else:
    print ("no puede votar")