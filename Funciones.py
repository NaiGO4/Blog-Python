#Funciones
#Llamadas a funciones

print("Llamadas a funciones")

print(type(32))#output: class 'int'  

print("---------------------------")
print("Funciones internas")
#Cuando utilizas max() y min() en una cadena de texto en Python, estos métodos devuelven el carácter que tiene el mayor y el menor valor ASCII respectivamente. 

#El código ASCII (American Standard Code for Information Interchange) es un estándar que asigna un número único a cada caracter, como letras, números, símbolos y otros caracteres especiales. Estos números permiten a los computadores representar y comunicar texto de manera consistente.

print(max("Hola mundo"))#output: u / "u" tiene un valor ASCII de 117.
print(min("Hola mundo"))#output: " " / " " (espacio) tiene un valor ASCII de 32.


def muestraDosVeces(bruce):
    print(bruce)
    print(bruce)

print(muestraDosVeces("Dos lineas"))
print(muestraDosVeces(11))


michael = "Michael, cantante"
print(muestraDosVeces(michael))
#El nombre de la variable que pasamos como argumento, (michael) no tiene nada que ver con el nombre del parámetro (bruce). 

#Ejercio

def fred():
    print("Zap")
def jane():
    print("ABC")

print(fred())
print(jane())
print(fred())