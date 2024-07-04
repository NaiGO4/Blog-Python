#Salto de linea
print("Salto de linea")
cosa = "Hola \nMundo"
print(cosa)

print("--------------------------")
print("Lectura de archivos")

man_archivo = open ("hola.txt")
contador = 0
for line in man_archivo:
    contador = contador + 1
print("Contador de lineas", contador)
print("--------------------------")
print(" BÚSQUEDA A TRAVÉS DE UN ARCHIVO ")

manejador_archivo = open('hola.txt')
inp = manejador_archivo.read()
print(len(inp))
print(inp[:20])

print("--------------------------")
manejador = open('hola.txt')
print(len(manejador.read()))


print("--------------------------")
print("Búsqueda a través de un archivo ")

man_a = open('hola.txt')
contador = 0
for linea in man_a:
    if linea.startswith('Hola'):
        print(linea)

print("--------------------------")
print("Permitiendo al usuario elegir el nombre de archivo")

narchivo = input('Ingresa un nombre de archivo: ')
man_a = open(narchivo)
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'líneas de asunto (subject) en', narchivo)