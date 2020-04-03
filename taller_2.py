"""resp=0
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
            print("numeros iguales a 0 y ",  mayor )"""
import current as current

"""cantidades=0
suma = 0
numCantidades = 0
while numCantidades <=10:
 cantidades= input("ingrese la cantidad\n")
 numCantidades+=1
 if numCantidades==10:
     for i in  cantidades: #numCantidades+=1
         suma = cantidades+cantidades
     print("la suma total de las cantiades es de :",suma)"""



"""promedioEdad = 0;
cantAlumnos = 0;
reiniciar = "no";
edades=[];
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
                continuar="si"""

"""a=1
b=1
print(a)
print(b)
i=0
n=10
while i<n:
    s=a+b
    a=b
    b=s
    print(s)
    i+=1"""


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

