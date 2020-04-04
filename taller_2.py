
                        # PUNTO/1

#Se requiere un algoritmo para obtener la edad promedio de un grupo de N alumnos. Si algún
#alumno tiene más de 18 años, se muestra el promedio que se lleva sin contar el alumno de 18
#años. EL usuario decide si desea cerrar el programa o vuelve a ejecutarlo.

"""promedioEdad = 0
cantAlumnos = 0
reiniciar = "no"
edades=[]
continuar="si"
while continuar == "si":
    edades = int(input("Bienvenid@ Estudiante cual es tu edad\n"))
    cantAlumnos+=1
    if edades >18:
        promedioEdad= (edades + edades)/cantAlumnos
        print("la cantidad de estuduantes encuestados es ", cantAlumnos)
        print("el promedio de edad es:",promedioEdad)
        cantAlumnos+=1
        continuar=input("deseas continuar\n")
        if continuar== "no":
            reiniciar=print("deseas reiniciar la encuesta")
            if continuar == "si":
                edades[cantAlumnos]
                cantAlumnos=0
                continuar="si"""""

                        # PUNTO/2

            # sumar diez cantidaddes diferentes mediante un ciclo for

"""suma = 0
for n in range(0,10):
numero = int(input("Digite el numero\n"))
suma = suma + numero
print("La suma  de los numeros es de :",suma)"""




                    # PUNTO/3


# Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo
# número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una
# estatura registrada.


""""promediestatura=0
numMiembros=0
estatura=0
reiniciar="no"
continuar="si"
while estatura <170:
     estatura=int(input("ingrese su estatura\n"))
estatura+=1
if estatura < 170:
         promediestatura= estatura + estatura / estatura
         print("la cantida de encuestados fueron:", numMiembros)
         print("el promedio de estatura es:", promediestatura)
         numMiembros+=1
continuar=input("deseas continuar\n")
if continuar == "no":
    reiniciar = input("deseas reiniciar\n")
    if continuar == "si":
        estatura[numMiembros]
        numMiembros=0
        continuar="si"""""







                        # PUNTO/4


#Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a
#cero y cuántas mayores a cero.
resp=0
cant=0
menor=0
igual=0
mayor=0
resp="si"

while resp == "si":
    cant=int(input("por favor ingrese una cantidad\n"))
    if cant < 0 :
        menor = menor + 1
    else:
        if cant == 0 :
            igual = igual + 1
        else:
            mayor = mayor + 1
            resp = input("desea ingresar otro valor\n")
            print("Se ingresaron", menor )
            print("numero menores a 0" , igual)
            print("numeros iguales a 0 y ",  mayor )


                # PUNTO/5


#Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran
#entre 0 y 100. Además muestre la multiplicación de todos estos.

"""sumapar = 0
sumaimp= 0
n = 0
for n in range(0,101,1):
if(n%2==0):
sumapar= sumapar +n
else:
sumaimp = sumaimp +n
multiplicacion = sumapar * sumaimp
print(multiplicacion)

            print(sumapar)
            print(sumaimp)"""

                        # PUNTO/6


# serie fibonacci

num1=1
num2=1
i=0
nun3=10
print(num1)
print(num2)
while i<nun3:
    suma=num1+num2
    num1=num2
    num2=suma

    print(suma)
    i+=1









