#Ejecución condicional
#Expresiones booleanas
#Una expresión booleana es aquella que puede ser verdadera (True) o falsa (False)

print("Expresiones booleanas")

x = 4 == 4 
y = 3 == 1
print(x)#output: true
print(y)#output: false
print(type(x))#output: bool

x != y # x es distinto de y
x > y # x es mayor que y
x < y # x es menor que y
x >= y # x es mayor o igual que y
x <= y # x es menor o igual que y
x is y # x es lo mismo que y
x is not y # x no es lo mismo que y

print("---------------------")
print("Operadores lógicos")
#Existen tres operadores lógicos: and (y), or (o), y not (no). 

a = 17 and True
print(a)#output: true


print("---------------------")
print("Ejecución condicional")
#Las sentencias condicionales nos proporcionan esa capacidad. La forma más sencilla es la sentencia if:

if x > 0:   
    print("x es positivo")

print("---------------------")
print("Ejecución alternativa")

if x%2 == 0:
    print("Es par")
else:
    print("No es par")#output: No es par

print("---------------------")
print("Condicionales encadenados")
#elif es una abreviatura para “else if”. En este caso también será ejecutada única-ente una de las ramas.
if x < y:
    print("x es mayor que y")
elif x > y:
    print("x es manor que y")
else:
    print("x e y son iguales")

print("---------------------")
print("Condicionales anidados")

#Un condicional puede también estar anidado dentro de otro. Podríamos haber escrito el ejemplo anterior de las tres ramas de este modo:

if x == y:
    print("x e y son iguales")
else:
    if x > y:
        print("x es menor que y")
    else:
        print("x es mayor que y")


print("---------------------")
print("Captura de excepciones usando try y except")

try:
    mi_diccionario = {"nombre": "Gian", "edad": 25}
    clave = input("Introduce la clave a buscar en el diccionario: ")
    valor = mi_diccionario[clave]
    print(f"El valor asociado a la clave '{clave}' es: {valor}")
except KeyError:
    print(f"Error: La clave '{clave}' no existe en el diccionario.")
