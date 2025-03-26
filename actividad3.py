'''
variable local:
Variable que sólo se puede utilizar en 1 bloque 


Actividad 3:
Elabore im programa que permita calcular el salario neto de un empleado
después de descontar los descuentos por conceptos de 


salud, pensión y ARL

El programa debe solicitar el tipo de empleado.

a - Empleado con contrato a término indefinido
b - Contrato por prestación de servicios
c - Contrato de aprendizaje
d - jornal (freelance)
    => se debe solicitar:
     -número de horas trabajadas
     -valor a pagar por hora
     *el total del salario se calcula de múltilicar el 
        (número de horas * valor a pagar por hora)
'''

contrato = input("Tipo de contrato: ")
salario_neto = 0
if contrato == "a":
    print ("Eligió: contrato a término indefinido")
elif contrato == "b":
    print ("Eligió: contrato por prestación de servicios")
elif contrato == "c":
    print ("Eligió: contrato de aprendizaje")
    min_salario = int(input("Ingrese salario mínimo legal vigente: git "))
    salario_neto = min_salario - (min_salario * 0.25)
elif contrato == "d":
    print ("Eligió: contrato por jornal (Freelance)")
    n_horas = int(input("¿cuántas horas trabajo?:"))
    v_horas = int(input("¿valor por hora de trabajo?:"))
    salario_neto = n_horas * v_horas
else:
    print ("Tipo de contrato inexistente")
print ("salario neto es: " , salario_neto)
print ("fin del programa")