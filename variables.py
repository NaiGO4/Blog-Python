#Valores y tipos
print('Valores y tipos')
#La sentencia print también funciona con enteros. Vamos a usar el comando pythonpara iniciar el intérprete.

print(4)#outpud = 3


#Si no estás seguro de qué tipo de valor estás manejando, el intérprete te lo puede decir.


print(type(''))#outpud = str
print(type(2))#outpud = int
print(type(2.1))#outpud = float


#Variables
print('-----------------')
print('Variables')
mensaje = 'Y ahora algo completamente diferente'
n = 17
pi = 3.1415926535897931

#Para mostrar el valor de una variable, se puede usar la sentencia print:
print(mensaje)#outpud = Y ahora algo completamente diferente
print(n)#outpud = 17
print(pi)#outpud = 3.1415926535897931


print('-----------------')
# NOMBRES DE VARIABLES Y PALABRAS CLAVES

print(type(mensaje))
print(type(n))#outpud = int
print(type(pi))#outpud = float

print('-----------------')
print('Sentencias')
#Una sentencia es una unidad de código que el intérprete de Python puede ejecutar.


print(1)#outpud 1
x = 2 
print(x)#outpud 2

print('-----------------')
print('Operadores y operandos')
#Los operadores son símbolos especiales que representan cálculos, como la suma o la multiplicación.

suma = 20 + 20
resta = 3 - 1
multiplicacion = 3 * 3
divicion = 3 / 1

print(suma)#outpud 40
print(resta)#outpud 2
print(multiplicacion)#outpud 9
print(divicion)#outpud 3.0

print('-----------------')
print('Expresiones')
#Expresiones
#Una expresión es una combinación de valores, variables y operadores. 

# Concatenación de cadenas
str1 = "Hola"
str2 = "Mundo"
q = str1 + " " + str2  # outpud: "Hola Mundo"

print('-----------------')
print('Orden de las operaciones')
#Orden de las operaciones
#Cuando en una expresión aparece más de un operador, el orden de evaluación depende de las reglas de precedencia.

#Los Paréntesis tienen el nivel superior de precedencia, y pueden usarse para forzar a que una expresión sea evaluada 
# en el orden que se quiera.
print(2 * (3-1) )#outpud: 4


#Ejercicio
nombre = input("Introdusca un nombre: ")

print("Bienvenido " + nombre)
