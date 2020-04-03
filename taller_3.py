"""Español=int(5)
Programacion=int(4)
Ingles=int(3)
Calculo=int(2)
Dibujo=int(1)

Notas={}

Notas["Español"]=[Español]
Notas["Programacion"]=[Programacion]
Notas["Ingles"]=[Ingles]
Notas["Calculo"]=[Calculo]
Notas["Dibujo"]=[Dibujo]
Notas=(Español+Programacion+Ingles+Calculo+Dibujo)

promedio=(Notas)/5
mayor=max(Notas)
print("el promedi del estudiante es:",promedio)"""


"""lista=[]
cantidad=int(input("cantidad\n"))
mayor=0
menor=0
i=1
while cantidad >0:
    numero = int(input("Numero #" + str(i) + ": \n"))
    lista.append(numero)
    i= i + 1
    cantidad = cantidad- 1
suma=cantidad+cantidad
mayor=max(lista)
menor=min(lista)
print("lista: ", lista)
print("Mayor: ", mayor)
print("Menor: ", menor)"""

# Detectar palindromos en una frase e imprimirlos
"""frase = "El señor Uruburu contruyó un radar. Ana, que tiene buen ojo, le dijo que ni con todo el oro del mundo le haría funcionar porque no tenía rotor." \
        " Uruburu tardó en reconocer su error."
# Primero quitamos todos los puntos y comas. Dejamos solo letrs y espacios.
def limpia(texto):
    limpio = ''
    for i in frase:
        if i != "." and i != ",":
            limpio += i
    return limpio
limpiado = limpia(frase)
# Creamos una lista con todas las palabras.
lista = limpiado.split()
# Función que detecta si una palabra es o no un palíndromo
def soyPalindromo(palabra):
    palabra = palabra.lower()
    soy = True  # inicialmente suponemos que si es un palíndromo
    n = len(palabra)
    if n % 2 == 0:  # número par de letras en la palabra
        for i in range(int(n / 2)):
            if palabra[i] != palabra[n - i - 1]:
                soy = False
    else:  # número impar de letras
        for i in range(int((n - 1) / 2)):
            if palabra[i] != palabra[n - i - 1]:
                soy = False
    return soy
# Pasamos todas las palabras de la lista por la función que detecta si son palíndromos
# Si se trata de un palindromo lo imprime en pantalla
for palabrita in lista:
    if soyPalindromo(palabrita):
        print(palabrita)"""


"""mensaje =Te alegrarás al saber que ningún desastre ha acompañado alinicio de una empresa que 
ha considerado con talmalos presentimientos.Llegué aquí ayer, y mi primera tarea 
para asegurarle a mi querida hermana mi bienestar y 
aumentar la confianza en El exito de mi empresa y el exito
Ya estoy muy al norte de Londres, y mientras camino por las calles dePetersburgh, siento que una brisa fría del norte juega en mis mejillas,
lo que refuerza mis nervios y me llena de deleite. Lo entiendes"
¿este sentimiento? Esta brisa, que ha viajado desde las regiones.""hacia donde avanzo me da un anticipo de esos climas helados
Inspirado por este viento de promesa, mis sueños se vuelven más fervientes
y vívido Intento en vano ser persuadido de que el poste es el asiento
de escarcha y desolación; alguna vez se presenta a mi imaginación como el
región de belleza y deleite. Allí, Margaret, el sol es siempre visible.
Su amplio disco bordea el horizonte y difunde un esplendor perpetuo.
Ahí, porque con tu permiso, hermana mía, pondré algo de confianza en lo anterior.
navegadores: allí se desvanecen la nieve y las heladas; y, navegando sobre un mar tranquilo,
podemos ser llevados a una tierra que supera las maravillas y la belleza de cada región
descubierto hasta ahora en el globo habitable. Sus producciones y características.
puede ser sin ejemplo, ya que los fenómenos de los cuerpos celestes sin duda
están en esas soledades no descubiertas. Lo que no se puede esperar en un país
de luz eterna? Puedo descubrir allí el maravilloso poder que atrae
la aguja y puede regular mil observaciones celestes que requieren
solo este viaje para que sus excentricidades aparentes sean consistentes para siempre.
Saciaré mi ardiente curiosidad con la vista de una parte del mundo
nunca antes visitado, y puede pisar una tierra nunca antes impresa por el
pie de hombre. Estos son mis atractivos, y son suficientes para conquistar
todo miedo al peligro o la muerte e inducirme a comenzar este laborioso viaje
con la alegría que siente un niño cuando se embarca en un pequeño bote, con sus vacaciones
compañeros, en una expedición de descubrimiento por su río natal. Pero suponiendo que todo
estas conjeturas son falsas, no puedes impugnar el beneficio inestimable
que conferiré a toda la humanidad, hasta la última generación, al descubrir
un pasaje cerca del polo a esos países, para llegar a lo que actualmente tantos
los meses son necesarios; o averiguando el secreto del imán, que,
si es posible, solo puede ser realizado por una empresa como la mía.
Estas reflexiones han disipado la agitación con la que comencé mi carta,
y siento que mi corazón brilla con un entusiasmo que me eleva al cielo
porque nada contribuye tanto a tranquilizar la mente como un propósito constante
- un punto en el que el alma puede fijar su ojo intelectual. Esta expedicion
Ha sido el sueño favorito de mis primeros años. He leido con ardor
Las cuentas de los diversos viajes que se han hecho en la perspectiva
de llegar al Océano Pacífico Norte a través de los mares que rodean
El polo. Puede recordar que una historia de todos los viajes realizados para
Los propósitos del descubrimiento compusieron toda la biblioteca de nuestro buen tío Thomas.
Mi educación fue descuidada, pero me apasionaba la lectura.
Estos volúmenes eran mi estudio día y noche, y mi familiaridad con ellos.
aumentó ese arrepentimiento que sentí, cuando era niño, al saber que mi
la orden de muerte de mi padre había prohibido a mi tío que me permitiera embarcar
en una vida marinera
Estas visiones se desvanecieron cuando examiné por primera vez a esos poetas.
cuyas efusiones cautivaron mi alma y la elevaron al cielo. Yo también
se convirtió en poeta y durante un año vivió en un paraíso de mi propia creación;
Me imaginé que también podría obtener un nicho en el templo donde el
Los nombres de Homero y Shakespeare están consagrados. Estas bien familiarizado
con mi fracaso y con cuánto cargué con la decepción. Pero solo en
esa vez heredé la fortuna de mi primo y mis pensamientos fueron
convertido en el canal de su anterior doblado.
Han pasado seis años desde que resolví mi empresa actual.
Incluso ahora puedo recordar la hora a partir de la cual me dediqué
Esta gran empresa. Comencé por hacer que mi cuerpo sufriera dificultades.
Acompañé a los pescadores de ballenas en varias expediciones al Mar del Norte;
Voluntariamente soporté el frío, el hambre, la sed y la falta de sueño;
A menudo trabajé más duro que los marineros comunes durante el día y dediqué
mis noches al estudio de las matemáticas, la teoría de la medicina,
y aquellas ramas de la ciencia física de las que naval
El aventurero podría obtener la mayor ventaja práctica.
Dos veces en realidad me contraté como un compañero menor en un ballenero de Groenlandia,
y me absolví a la admiración. Debo reconocer que me sentí un poco orgulloso
cuando mi capitán me ofreció la segunda dignidad en el barco y
me suplicó que me quedara con la mayor seriedad, tan valioso
¿Consideró mis servicios? Y ahora, querida Margaret, ¿no merezco
para lograr un gran propósito? Mi vida podría haber pasado fácilmente
y lujo, pero preferí la gloria a cada incentivo que la riqueza colocaba
en mi camino ¡Oh, que alguna voz alentadora respondiera afirmativamente!
Mi coraje y mi resolución son firmes; pero mis esperanzas fluctúan y mi espíritu
a menudo están deprimidos Estoy a punto de continuar un viaje largo y difícil.
cuyas emergencias demandarán toda mi fortaleza: soy requerido
no solo para elevar el espíritu de los demás, sino a veces para mantener el mío,
cuando el suyo está fallando.
Este es el período más favorable para viajar en Rusia. Ellos vuelan
rápidamente sobre la nieve en sus trineos; el movimiento es agradable y
en mi opinión, mucho más agradable que el de una diligencia inglesa.
El frío no es excesivo si estás envuelto en pieles, un vestido que
Ya he adoptado, porque hay una gran diferencia entre caminar
la cubierta y el resto del asiento permanecen inmóviles durante horas, cuando no hay ejercicio
evita que la sangre se congele en tus venas. No tengo
ambición de perder mi vida en el camino posterior entre St. Petersburgh
y Arcángel Partiré a la última ciudad dentro de quince días.
o tres semanas; y mi intención es alquilar un barco allí, que puede
se puede hacer fácilmente pagando el seguro del propietario y contratando
tantos marineros como creo necesarios entre los que están acostumbrados
a la pesca de ballenas. No tengo intención de navegar hasta el mes de junio;
y cuando debo volver? Ah, querida hermana, ¿cómo puedo responder esta pregunta?
Si tengo éxito, pasarán muchos, muchos meses, quizás años, antes que tú
y puedo encontrarme. Si fallo, me verás de nuevo pronto o nunca.
Adiós, querida, excelente Margaret. El cielo derrama bendiciones
en ti, y sálvame, para que pueda testificar una y otra vez mi gratitud
por todo tu amor y amabilidad."""
"""resultado=mensaje.count("e")
print(resultado)"""

"""def mostrar_vocales(frase):
    vocales="aeiou"
    return [c for c in frase if c in vocales]
texto=input("ingres un texto\n")
print(mostrar_vocales(texto))"""

"""def leer_frase():
    global txt
    txt=input("Ingrese una frase:\n").lower()
def contar_vocales():
       vocal=["a", "e", "i", "o", "u"]
       cont=0
       for i in vocal:
           for h in txt:
               if i ==h:
                   cont+=1
       print("El numero de vocales es:",cont)
leer_frase()
contar_vocales()"""


"""vocales=("a", "e", "i", "o", "u")
texto=input("Ingrese un texto:\n")
nuevo_texto=""
for letras in texto:
    if letras not in vocales:
        nuevo_texto = nuevo_texto + letras
print("El texto sin vocales es:".format(nuevo_texto),nuevo_texto)
print("la longitud es:",len(nuevo_texto))"""


"""def par(num):
    if(num%2==0):
        return True
    else:
        False
def main():
    lista = []
    i = 0
    while(i<10):
        num=(int(input("Ingrese un numero par: \n")))
        if(par(num)):
            lista.append(num)
            i+=1
    print(lista)
if __name__ == '__main__':
    main()"""






