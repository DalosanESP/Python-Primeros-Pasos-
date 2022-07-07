print("Hola Mundo")
print("Hello Word")

#Comentario de codigo
print("Me llamo Dalosan")

"""
Texto que no se va a interpretar
aunque este en diferentes lineas
"""

# Variables
texto = "Primera Variable de Texto"
texto2 = "Segunda Variable de Texto"

año = 2022
 
#concatenar variables
print(f"{texto} - {texto2}")

#concatenar variables (string y numero)
print(f"{texto} - {texto2} - {str(año)}")

#Otra manera de concatenar. Siempre con el mismo tipo de dato (En el caso de la variable año, con la funcion str, cambiamos el formato de esa variable a un string)
print(texto + " - " + texto2 + " - " + str(año))

#Entrada de Datos
sitioweb = input("¿Cual es tu página web?: ")
print ("El sitio web del usuario es " + sitioweb)

#Condiciones
altura = int(input("¿Cual es tu altura?"))
if altura >= 180:
    print("Eres una persona alta")
else:
    print("No eres una persona muy alta")

#Funciones
"""
Para indicar una funcion debemos ponerle def delante
"""
def mostrarAltura():
    altura2 = int(input("¿Cuantos cm mides?"))
    if altura2 >= 175:
        print("Eres alto")
    else:
        print("Eres bajito")

mostrarAltura()
mostrarAltura()
mostrarAltura()

#En este caso solo nos preguntara una vez, ya que estamos pasandole todo el rato la misma altura, y nos mostrara el resultado tantas veces como repitamos la funcion
var_altura3 = int(input("¿Cual es tu altura en centimetros?"))

def mostrarAltura(altura3):

    if altura3 >= 175:
        print("Eres alto")
    else:
        print("Eres bajito")

mostrarAltura(var_altura3)
mostrarAltura(var_altura3)
mostrarAltura(var_altura3)

#Ahora con return
var_altura4 = int(input("¿Cual es tu altura en centimetros?"))

def mostrarAltura2(altura4):
    resultado = ""

    if altura4 >= 175:
        resultado = "Eres una persona alta"
    else:
        resultado = "Eres una persona baja"

    return resultado

print(mostrarAltura2(var_altura4))

#Listas
personas = ["Obi-Wan","Anakin","Ahsoka"]
print(personas[0])

#Persona es el nombre del bucle, que tambien es una variable
for persona in personas:
    print("-" + persona)