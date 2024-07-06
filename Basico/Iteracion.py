#La sentencia while

n = 5
while n > 0:
    print(n)
    n = n - 1
    print("Despege")

#“Bucles infinitos” y break

print("------------------------")
print("“Bucles infinitos” y break")
"""
n = 10
while True:
    print(n, end= ' ')
    n = n - 1
print("Terminado")#infinito
"""

print("------------------------")
print("Bucles con break")
#Cada vez que se entre en el bucle, se pedirá una entrada al usuario. Si el usuario escribe fin, la sentencia break hará que se salga del bucle.

"""
while True:
    linea = input('> ')
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado!')
"""
print("------------------------")
print("“Bucles utilizando continue")
while True:
    linea = input('> ')
    if linea[0] == '#' :
        continue
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado!')

print("-------------------------")
print("Bucles definidos usando for")

animales = ["gato", "perro", "loro"]
for animal in animales:
    print("Mascota:", animal)
print("Terminado")