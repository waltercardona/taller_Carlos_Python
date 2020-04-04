
# Dados los valores ingresados por el usuario
# (base, altura) mostar en pantalla el area de un triangula

base=int(input("ingrese el base del triangulo\n"))
altura=int(input("ingrese la altura del triangulo\n"))
area = base * altura / 2
print("el area es del triangulo es :",area)


# Convertir la cantidad de dolares
# ingresados por el usaurio
# a pesos colombianos y mostrar en pantalla el resultado

"""dolares=int(input("ingrese la cantidad de dolares\n"))
valor_pesos=int(input("valor en pesos Colombianos\n"))
resultado=dolares*valor_pesos
print("el valor es:",resultado)"""

# convertir los grados centigrados ingresados
# por un usaurio a grados fahreinhait y mostrar el resultado
# en pantalla

"""grados_centigrados=float(input("ingrese los centigrados:\n"))
grados_fahrenheit= (grados_centigrados*(9/5))+32
print(grados_centigrados ,"Grados centigrados: Los grados centigrados convertidos a grados fahrenheit es  :",grados_fahrenheit , "grados fahrenheit")"""


# mostrar en pantalla la cantidad de segundos que tiene un lustro

"""años=int(5)
dias=int(365)
horas=int(24)
minutos=int(60)
segundos=int(60)
dia_biciesto =int(86400)
lustro=(segundos*minutos*horas*dias*años) + dia_biciesto
print("la cantidad de segundos que tiene un lustro es:",lustro, " millones de segundos")"""

#calcular la cantidad de segundos que le toma viajar la luz del sol a marte y mos trarlo en pantalla

"""distancia_sol_marte=227940000 # millones de kilometros
velocidad_luz=300000 # m/s
total_segundos=int(distancia_sol_marte/velocidad_luz)
minutos = 60
total_minutos =int(total_segundos/minutos)
print("la cantidad de segundos que se demora en viajar la luz del sol a marte es de:",total_segundos, " segundos")
print("la cantidad de minutos  que se demora en viajar la luz del sol a marte es de :",total_minutos, "minutos")"""

# calcular el numero de vueltas que da una llanta en 1km, dado que el diametro es de 50cm,
# mostrar el resulktado en pantalla

"""centimetros=100000
diametro_llanta=int(50)
total_vueltas=centimetros/diametro_llanta
print("la cantidad de vuelta que dio la llanta es:",total_vueltas, "vueltas")"""

# mostrar en pantalla la cantidad de meses trascurridos desde la fecha de nacimienro de un usaurio

"""from datetime import  date

def cantidad_meses (fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    meses = resultado * 12

    return  meses

fecha_nacimiento_walter = date(1986,10,10)
meses = cantidad_meses(fecha_nacimiento_walter)

print(" la cantidad de meses  de walter es de :", meses, "meses")"""

# profe esta es la forma de conseguir los dias desde mi fecha de nacimiento

"""from datetime import date

hoy = date.today()
otra_fecha = date(1986,10,10)
dias = hoy - otra_fecha

print (dias)"""

# calcular y mostrar en pantalla la longitud de la sombra de un edificio de 20 metros
# de altura cuando el angulo que forma los rayos del sol con el suelo es de 22º

"""import math
altura=20
angulo=float(math.radians(22))
angulo1=math.radians(angulo)
sombra=altura/math.tan(22)
print(sombra)"""

# mostrar en pantalla True o false si la edad ingresada por dos usaurios es la misma

"""edad_1=int(input("ingrese edad uno:\n"))
edad_2=int(input("ingrese  edad dos:\n"))
igual=edad_1==edad_2
print(igual)"""

# mostrar en pantalla el promedio de un alumno que ha cursado 5 materias
# (español, matematicas, programacion, economia, ingles)

"""español=float(input("nota de Español:\n"))
matematicas=float(input("nota de Matematicas:\n"))
economia=float(input("nota de Economia:\n"))
programacion=float(input("nota de Programacion:\n"))
ingles=float(input("nota de Ingles:\n"))

promedio= (español + matematicas + economia + programacion + ingles)/5
print("tu promedio es",promedio)"""

