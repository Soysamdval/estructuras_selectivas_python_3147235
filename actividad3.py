'''
variable local:
Variable que sólo se puede utilizar en 1 bloque 


Actividad 3:
Elabore im programa que permita calcular el salario neto de un empleado
después de descontar los descuentos por conceptos de 


salud, pensión y ARL

El programa debe solicitar el tipo de empleado.

a - Empleado con contrato a término indefinido
        -antiguedad en años
        -grado o escalafon (1 - 5)
        -el salario minimo
        Se calcula a la siguiente tabla:
            -grado 1= 1.5 sm
            -grado 2= 1.7 sm
            -grado 3 2.0 sm
            -grado 4 2.5 sm
            -grado 5 3.0 sm
        la bonificación es acorde a los siguientes rangos antiguedad:
            -1 - 5 años: 1%
            -6- 10 años: 2%
            - > 10 años: 3%
        Descuentos de ley:
        - 25% eps
        - 22% pension
        - 0.1% ARL
b - Contrato por prestación de servicios
    -valor de contrato
    -numero de meses de contrato
    -la antiguedad del empleado (años)
    Salario neto se calcula:
    1. dividir el contrato
        por el número de meses

    2. restar el 15% de salario mensual,
        por concepto de EPS (salud)

    3. restar el 10% del valor del salario mensual 
        por concepto de prensión

    4. si el empleado tiene una antiguedad >= 10 años:
        tendrá bonificación del 0,5%
        sobre el salario mensual

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
    min_salario = int(input("Ingrese el salario mínimo: "))

    antiguedad = int(input("Tiempo que ha trabajado: "))
    eps = 0.25
    pension = 0.22
    arl = 0.1
    
    if antiguedad <= 5:
        salario_neto + 0.01
    elif antiguedad <= 10:
        salario_neto + 0.02
    elif antiguedad >=10:
        salario_neto + 0.3

    grado = int(input("grado en el cual está: "))
    if grado == 1:
       salario_neto = min_salario + 1.5
    elif grado == 2:
        salario_neto = min_salario + 1.7
    elif grado == 3:
        salario_neto = min_salario + 2.0
    elif grado == 4:
        salario_neto = min_salario + 2.5
    elif grado == 5:
        salario_neto = min_salario + 3.0
    total = salario_neto

elif contrato == "b":
    print ("Eligió: contrato por prestación de servicios")
    valor_contrato = int(input("ingrese valor del contrato "))
    n_meses = int(input("número de meses "))
    antiguedad = int(input("Tiempo de antiguedad "))
    salario_mensual = valor_contrato / n_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.05
    salario_neto = salario_mensual - eps -pension
    if antiguedad >=10:
        salario_neto = salario_mensual + bonificacion

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